import os
import json
import requests
import subprocess
import openai
import nbformat as nbf
import hashlib
from tabulate import tabulate
import argparse

def find_files_in_folder(folder_path, extension, exclude=[]):
    files = []
    for root, _, filenames in os.walk(folder_path):
        if root in exclude:
            continue
        for file in filenames:
            if file.endswith(f".{extension}"):
                files.append(os.path.join(root, file))
    return files

def get_current_commit_hash():
    try:
        result = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
        commit_hash = result.decode().strip()
        return commit_hash
    except subprocess.CalledProcessError:
        return None

def get_current_branch():
    try:
        result = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        branch = result.decode().strip()
        return branch
    except subprocess.CalledProcessError:
        return None

def is_link_valid(url):
    try:
        r = requests.head(url)
        return r.status_code == 200
    except:
        return False

def check_json(model):
    
    check_list = ["name", "algorithm", "version", "category", "config", "dataset", "classes", "image", "description", "network", "benchmark"]
    for item in check_list:
        if item not in model:
            raise ValueError("Missing key: {}".format(item))
    
    for item in model["benchmark"]:
        if is_link_valid(item["url"]) == False:
            raise ValueError("Invalid link: {}".format(item["url"]))
        
def get_file_md5(file_path):
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return  "md5:"+hash

def download_file(url, folder_path):
    local_filename = os.path.join(folder_path, url.split('/')[-1])
    print("Downloading {} to {}".format(url, local_filename))
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def generate_doc_zh_CN(model):
    
    branch = get_current_branch()
    object_name = "{}_{}_{}".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_'), model["network"]["input"]["shape"][0])
    
    doc = ""
    
    # 添加模型名称和描述
    doc += "# {} - {}\n\n".format(model["name"], model["algorithm"])
    
    # Add en
    doc += "[English](../en/{}.md) | 简体中文 ".format(object_name)
    
    # 添加Colab徽章
    doc += "[![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/{}/notebooks/zh_CN/{}.ipynb)\n\n".format(branch, object_name)


    # 添加模型徽章
    doc += "**版本：** {}\n\n".format(model["version"])
    doc += "**任务** {}\n\n".format(model["category"])
    doc += "**算法：** [{}]({})\n\n".format(model["algorithm"],  "https://github.com/Seeed-Studio/ModelAssistant/blob/main/" + model["config"]["url"])
    doc += "**数据集：** [{}]({})\n\n".format(model["dataset"]["name"], model["dataset"]["url"])

    # 添加类别
    doc += "**类别** "
    doc += ", ".join(["`{}`".format(c) for c in model["classes"]]) + "\n\n"

    # 添加模型图片
    doc += "![{}]({})\n\n".format(model["name"], model["image"])
        
    # 添加模型描述
    doc += model["description"] + "\n\n"
    
    # 添加网络架构
    doc += "### 网络架构\n\n"
    network = model["network"]
    network_headers = ["", "类型", "批次", "形状", "备注"]
    network_table = []
    network_table.append(["输入", network["input"]["type"], network["batch"], network["input"]["shape"], network["input"].get("remark", "")])   
    network_table.append(["输出", network["output"]["type"], network["batch"], network["output"]["shape"], network["output"].get("remark", "")])
    doc += tabulate(network_table, network_headers, tablefmt="pipe", numalign="center", floatfmt=".2f") + "\n"
        
    # 添加基准测试
    doc += "### 基准测试\n\n"
    benchmark_headers = ["框架", "精度"]
    benchmark_table = []
    metrics_headers = []
    inference = []
        
    benchmarks = model["benchmark"]
    for benchmark in benchmarks:
        metrics = benchmark.get("metrics", {})
        for key, value in metrics.items():
            if key == "Inference(ms)":
                for k, v in value.items():
                    if k not in inference:
                        inference.append(k)
            if key not in metrics_headers:
                metrics_headers.append(key)

    for key in metrics_headers:
        benchmark_headers.append(key)
        
    benchmark_headers.append("下载")
    benchmark_headers.append("作者")
        
    for benchmark in benchmarks:
        backend = benchmark.get("backend", "")
        precision = benchmark.get("precision", "")
        metrics = benchmark.get("metrics", {})
        link = "[链接]({})".format(benchmark.get("url", ""))
        author = benchmark.get("author", "")
        benchmark_table.append([backend, precision])
        for key in metrics_headers:
            if key in metrics:
                if key == "Inference(ms)":
                    benchmark_table[-1].append("<br>".join([str("{}<sup>({})</sup>".format(metrics[key].get(k, "-"), inference.index(k)+1)) for k in metrics[key]]))
                else:
                    benchmark_table[-1].append(metrics[key])
            else:
                benchmark_table[-1].append("-") 
                    
        benchmark_table[-1].append(link)
        benchmark_table[-1].append(author)
            
    doc += tabulate(benchmark_table, benchmark_headers, tablefmt="pipe", numalign="center", stralign="center", floatfmt=".2f") + "\n"
        
    # 添加表格注释
    doc += "\n"
    doc += "***表格注释：***\n\n"
    if "benchmark_note" in model:
        for key, value in model["benchmark_note"].items():
            doc += "- ***{}：*** {}.*\n".format(key, value)
    doc += "- ***框架：** 用于推断模型的深度学习框架.*\n"
    doc += "- ***精度：** 用于训练模型的数值精度.*\n"
    doc += "- ***指标：** 用于评估模型的指标.*\n"
    doc += "- ***推理时间（毫秒）：** 模型的推理时间（以毫秒为单位）.*\n"
    for i, key in enumerate(inference):
        doc += "  - ***{}：** {}.*\n".format(i+1, key)
    doc += "- ***链接：** 模型的链接.*\n"
    doc += "- ***作者：** 模型的作者.*\n"
    doc += "\n"
        
    # 添加使用指南
    doc += "## 使用指南\n\n"
    if model.get("guidelines", "") != "":
        doc += model.get("guidelines", "")
        
    # 添加许可证
    doc += "### 许可证\n\n"
    doc += model.get("license", "")
    doc += "\n\n"
        
    return doc

def generate_doc_en(model):
    
    branch = get_current_branch()
    object_name = "{}_{}_{}".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_'), model["network"]["input"]["shape"][0])
    
    
    doc = ""
    
    # Add model name and description
    doc += "# {} - {}\n\n".format(model["name"], model["algorithm"])
    
    # Add zh_CN
    doc += "English | [简体中文](../zh_CN/{}.md) ".format(object_name)
    
    # Add Colab Badge
    doc += "[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/{}/notebooks/en/{}.ipynb)\n\n".format(branch, object_name)


    # Add model badges
    doc += "**Version:** {}\n\n".format(model["version"])
    doc += "**Category:** {}\n\n".format(model["category"])
    doc += "**Algorithm:** [{}]({})\n\n".format(model["algorithm"], model["config"]["url"])
    doc += "**Dataset:** [{}]({})\n\n".format(model["dataset"]["name"], model["dataset"]["url"])

    # Add class
    doc += "**Class:** "
    doc += ", ".join(["`{}`".format(c) for c in model["classes"]]) + "\n\n"

    # Add model image
    doc += "![{}]({})\n\n".format(model["name"], model["image"])
        
    #Add model description
    doc += model["description"] + "\n\n"
    
    # Add Network Architecture
    doc += "### Network \n\n"
    network = model["network"]
    network_headers = ["", "Type", "Batch", "Shape", "Remark"]
    network_table = []
    network_table.append(["Input", network["input"]["type"], network["batch"], network["input"]["shape"], network["input"].get("remark", "")])   
    network_table.append(["Output", network["output"]["type"], network["batch"], network["output"]["shape"], network["output"].get("remark", "")])
    doc += tabulate(network_table, network_headers, tablefmt="pipe", numalign="center", floatfmt=".2f") + "\n"
        
    # Add Benchmark benchmark_table
    doc += "### Benchmark\n\n"
    benchmark_headers = ["Backend", "Precision"]
    benchmark_table = []
    metrics_headers = []
    inference = []
        
    benchmarks = model["benchmark"]
    for benchmark in benchmarks:
        metrics = benchmark.get("metrics", {})
        for key, value in metrics.items():
            if key == "Inference(ms)":
                for k, v in value.items():
                    if k not in inference:
                        inference.append(k)
            if key not in metrics_headers:
                metrics_headers.append(key)

    for key in metrics_headers:
        benchmark_headers.append(key)
        
    benchmark_headers.append("Download")
    benchmark_headers.append("Author")
        
    for benchmark in benchmarks:
        backend = benchmark.get("backend", "")
        precision = benchmark.get("precision", "")
        metrics = benchmark.get("metrics", {})
        link = "[Link]({})".format(benchmark.get("url", ""))
        author = benchmark.get("author", "")
        benchmark_table.append([backend, precision])
        for key in metrics_headers:
            if key in metrics:
                if key == "Inference(ms)":
                    benchmark_table[-1].append("<br>".join([str("{}<sup>({})</sup>".format(metrics[key].get(k, "-"), inference.index(k)+1)) for k in key]))
                else:
                    benchmark_table[-1].append(metrics[key])
            else:
                benchmark_table[-1].append("-") 
                    
        benchmark_table[-1].append(link)
        benchmark_table[-1].append(author)
            
    doc += tabulate(benchmark_table, benchmark_headers, tablefmt="pipe", numalign="center", stralign="center", floatfmt=".2f") + "\n"
        
    # Add Table Notes
    doc += "\n"
    doc += "***Table Notes:***\n\n"
    if "benchmark_note" in model:
        for key, value in model["benchmark_note"].items():
            doc += "- ***{}:** {}.*\n".format(key, value)
    doc += "- ***Backend:** The deep learning framework used to infer the model.*\n"
    doc += "- ***Precision:** The numerical precision used for training the model.*\n"
    doc += "- ***Metrics:** The metrics used to evaluate the model.*\n"
    doc += "- ***Inference(ms):** The inference time of the model in milliseconds.*\n"
    for i, key in enumerate(inference):
        doc += "  - ***{}:** {}.*\n".format(i+1, key)
    doc += "- ***Link:** The link to the model.*\n"
    doc += "- ***Author:** The author of the model.*\n"
    doc += "\n"
        
    # Add Guidelines
    if model.get("guidelines", "") != "":
        doc += "## Guidelines\n\n"
        doc += model.get("guidelines", "")
        
    # Add License
    doc += "### License\n\n"
    doc += model.get("license", "")
    doc += "\n\n"
        
    return doc

def generate_notebook_en(model):
    branch = get_current_branch()
    object_name = "{}_{}_{}".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_'), model["network"]["input"]["shape"][0])
    config = model.get("config", "")
    config_file = config.get("url", "config.py")
    benchmark = [item for item in model.get("benchmark", {}) if item.get('backend') == "PyTorch"]
    pretrain_url = benchmark[0].get("url", "")
    dataset_url = model.get("dataset", {}).get("download", "")
    work_dir = "{}_{}_{}".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_'), model["network"]["input"]["shape"][0])
    height = model["network"]["input"]["shape"][0]
    width = model["network"]["input"]["shape"][1]
    
    file = open(os.path.join(os.getcwd(), "templates", "notebook.template.en.ipynb"))
    if file is None:
        raise ValueError("Invalid notebook template file")
    notebook = nbf.read(file, as_version=4)
    
    model_info = ""
    model_info += "# {} - {}\n\n".format(model["name"], model["algorithm"])
    model_info += "[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/{}/notebooks/en/{}.ipynb)\n\n".format(branch, object_name)
    model_info += "**Version:** {}\n\n".format(model["version"])
    model_info += "**Category:** {}\n\n".format(model["category"])
    model_info += "**Algorithm:** [{}]({})\n\n".format(model["algorithm"], model["config"]["url"])
    model_info += "**Dataset:** [{}]({})\n\n".format(model["dataset"]["name"], model["dataset"]["url"])
    model_info += "**Class:** "
    model_info += ", ".join(["`{}`".format(c) for c in model["classes"]]) + "\n\n"
    model_info += "![{}]({})\n\n".format(model["name"], model["image"])
    model_info += model["description"] + "\n\n"
    
    notebook['cells'][1]['source'] = model_info
    
    # Prepare Pretrain
    notebook['cells'][5]['source'] = '%mkdir -p {} \n'.format(work_dir)
    notebook['cells'][5]['source'] += '!wget -c {} -O {}/pretrain.pth'.format(pretrain_url, work_dir)
    
    # Prepare Dataset
    notebook['cells'][7]['source'] = '%mkdir -p {}/dataset \n'.format(work_dir)
    if dataset_url != "":
        notebook['cells'][7]['source'] += '!wget -c {} -O {}/dataset.zip \n'.format(dataset_url, work_dir)
        notebook['cells'][7]['source'] += '!unzip -q {}/dataset.zip -d {}/dataset'.format(work_dir,work_dir)
    else:
        notebook['cells'][7]['source'] += "# Auto Fetch By ModelAssistant"
        
    
    cfg_options = '''--cfg-options  \\
    work_dir={} \\
    num_classes={} \\
    epochs=10 '''.format(work_dir, len(model["classes"]))
    
    if model["network"]["input"]["type"] == "image":
        cfg_options += " \\\n    height={} \\\n    width={}".format(height, width)
    if dataset_url != "":
        cfg_options += " \\\n    data_root={}/dataset/".format(work_dir)
    if pretrain_url != "":
        cfg_options += " \\\n    load_from={}/pretrain.pth".format(work_dir)
    if config.get("argument", "") != "":
        cfg_options += " \\\n    {}".format(config.get("argument", ""))

    # Train Model 
    if config != "":
        notebook['cells'][9]['source'] = "!sscma.train {} \\\n{}".format(config_file, cfg_options)

        # Export Model
        notebook['cells'][11]['source'] = "import os\n"
        notebook['cells'][11]['source'] += "with open('{}/last_checkpoint', 'r') as f:\n\tos.environ['CHECKPOINT_FILE_PATH'] = f.read()".format(work_dir)
        notebook['cells'][12]['source'] = "!sscma.export {} $CHECKPOINT_FILE_PATH {}".format(config_file, cfg_options)
        notebook['cells'][15]['source'] = "!sscma.inference {} ${{CHECKPOINT_FILE_PATH%.*}}.pth \\\n{}".format(config_file, cfg_options)
        notebook['cells'][17]['source'] = "!sscma.inference {} ${{CHECKPOINT_FILE_PATH%.*}}_float32.onnx \\\n{}".format(config_file, cfg_options)
        notebook['cells'][19]['source'] = "!sscma.inference {} ${{CHECKPOINT_FILE_PATH%.*}}_float32.tflite \\\n{}".format(config_file, cfg_options)
        notebook['cells'][21]['source'] = "!sscma.inference {} ${{CHECKPOINT_FILE_PATH%.*}}_int8.tflite \\\n{}".format(config_file, cfg_options)
        notebook['cells'][23]['source'] = "%ls -lh {}/".format(work_dir)

    return notebook


def generate_doc_en(model):
    
    branch = get_current_branch()
    object_name = "{}_{}_{}".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_'), model["network"]["input"]["shape"][0])
    
    
    doc = ""
    
    # Add model name and description
    doc += "# {} - {}\n\n".format(model["name"], model["algorithm"])
    
    # Add zh_CN
    doc += "English | [简体中文](../zh_CN/{}.md) ".format(object_name)
    
    # Add Colab Badge
    doc += "[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/{}/notebooks/en/{}.ipynb)\n\n".format(branch, object_name)


    # Add model badges
    doc += "**Version:** {}\n\n".format(model["version"])
    doc += "**Category:** {}\n\n".format(model["category"])
    doc += "**Algorithm:** [{}]({})\n\n".format(model["algorithm"],  "https://github.com/Seeed-Studio/ModelAssistant/blob/main/" + model["config"]["url"])
    doc += "**Dataset:** [{}]({})\n\n".format(model["dataset"]["name"], model["dataset"]["url"])

    # Add class
    doc += "**Class:** "
    doc += ", ".join(["`{}`".format(c) for c in model["classes"]]) + "\n\n"

    # Add model image
    doc += "![{}]({})\n\n".format(model["name"], model["image"])
        
    #Add model description
    doc += model["description"] + "\n\n"
    
    # Add Network Architecture
    doc += "### Network \n\n"
    network = model["network"]
    network_headers = ["", "Type", "Batch", "Shape", "Remark"]
    network_table = []
    network_table.append(["Input", network["input"]["type"], network["batch"], network["input"]["shape"], network["input"].get("remark", "")])   
    network_table.append(["Output", network["output"]["type"], network["batch"], network["output"]["shape"], network["output"].get("remark", "")])
    doc += tabulate(network_table, network_headers, tablefmt="pipe", numalign="center", floatfmt=".2f") + "\n"
        
    # Add Benchmark benchmark_table
    doc += "### Benchmark\n\n"
    benchmark_headers = ["Backend", "Precision"]
    benchmark_table = []
    metrics_headers = []
    inference = []

    benchmarks = model["benchmark"]
    for benchmark in benchmarks:
        metrics = benchmark.get("metrics", {})
        for key, value in metrics.items():
            if key == "Inference(ms)":
                for k, v in value.items():
                    if k not in inference:
                        inference.append(k)
            if key not in metrics_headers:
                metrics_headers.append(key)

    for key in metrics_headers:
        benchmark_headers.append(key)
        
    benchmark_headers.append("Download")
    benchmark_headers.append("Author")
        
    for benchmark in benchmarks:
        backend = benchmark.get("backend", "")
        precision = benchmark.get("precision", "")
        metrics = benchmark.get("metrics", {})
        link = "[Link]({})".format(benchmark.get("url", ""))
        author = benchmark.get("author", "")
        benchmark_table.append([backend, precision])
        for key in metrics_headers:
            if key in metrics:
                if key == "Inference(ms)":
                    benchmark_table[-1].append("<br>".join([str("{}<sup>({})</sup>".format(metrics[key].get(k, "-"), inference.index(k)+1)) for k in metrics[key]]))
                else:
                    benchmark_table[-1].append(metrics[key])
            else:
                benchmark_table[-1].append("-") 
                    
        benchmark_table[-1].append(link)
        benchmark_table[-1].append(author)
            
    doc += tabulate(benchmark_table, benchmark_headers, tablefmt="pipe", numalign="center", stralign="center", floatfmt=".2f") + "\n"
        
    # Add Table Notes
    doc += "\n"
    doc += "***Table Notes:***\n\n"
    if "benchmark_note" in model:
        for key, value in model["benchmark_note"].items():
            doc += "- ***{}:** {}.*\n".format(key, value)
    doc += "- ***Backend:** The deep learning framework used to infer the model.*\n"
    doc += "- ***Precision:** The numerical precision used for training the model.*\n"
    doc += "- ***Metrics:** The metrics used to evaluate the model.*\n"
    doc += "- ***Inference(ms):** The inference time of the model in milliseconds.*\n"
    for i, key in enumerate(inference):
        doc += "  - ***{}:** {}.*\n".format(i+1, key)
    doc += "- ***Link:** The link to the model.*\n"
    doc += "- ***Author:** The author of the model.*\n"
    doc += "\n"
        
    # Add Guidelines
    if model.get("guidelines", "") != "":
        doc += "## Guidelines\n\n"
        doc += model.get("guidelines", "")
        
    # Add License
    doc += "### License\n\n"
    doc += model.get("license", "")
    doc += "\n\n"
        
    return doc

def generate_notebook_zh_CN(model):
    branch = get_current_branch()
    config = model.get("config", "")
    config_file = config.get("url", "config.py")
    benchmark = [item for item in model.get("benchmark", {}) if item.get('backend') == "PyTorch"]
    pretrain_url = benchmark[0].get("url", "")
    dataset_url = model.get("dataset", {}).get("download", "")
    work_dir = "{}_{}_{}".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_'), model["network"]["input"]["shape"][0])
    height = model["network"]["input"]["shape"][0]
    width = model["network"]["input"]["shape"][1]
    
    file = open(os.path.join(os.getcwd(), "templates", "notebook.template.zh_CN.ipynb"))
    if file is None:
        raise ValueError("Invalid notebook template file")
    notebook = nbf.read(file, as_version=4)
    
    model_info = ""
    model_info += "# {} - {}\n\n".format(model["name"], model["algorithm"])
    model_info += "[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/{}/notebooks/en/{}.ipynb)\n\n".format(branch, work_dir)
    model_info += "**版本:** {}\n\n".format(model["version"])
    model_info += "**任务:** {}\n\n".format(model["category"])
    model_info += "**算法:** [{}]({})\n\n".format(model["algorithm"], model["config"]["url"])
    model_info += "**数据集:** [{}]({})\n\n".format(model["dataset"]["name"], model["dataset"]["url"])
    model_info += "**类别:** "
    model_info += ", ".join(["`{}`".format(c) for c in model["classes"]]) + "\n\n"
    model_info += "![{}]({})\n\n".format(model["name"], model["image"])
    model_info += model["description"] + "\n\n"
    
    notebook['cells'][1]['source'] = model_info
    
    # Prepare Pretrain
    notebook['cells'][5]['source'] = '%mkdir -p {} \n'.format(work_dir)
    notebook['cells'][5]['source'] += '!wget -c {} -O {}/pretrain.pth'.format(pretrain_url, work_dir)
    
    # Prepare Dataset
    notebook['cells'][7]['source'] = '%mkdir -p {}/dataset \n'.format(work_dir)
    if dataset_url != "":
        notebook['cells'][7]['source'] += '!wget -c {} -O {}/dataset.zip \n'.format(dataset_url, work_dir)
        notebook['cells'][7]['source'] += '!unzip -q {}/dataset.zip -d {}/dataset'.format(work_dir,work_dir)
    else:
        notebook['cells'][7]['source'] += "# Auto Fetch By ModelAssistant"
        
    
    cfg_options = '''--cfg-options  \\
    work_dir={} \\
    num_classes={} \\
    epochs=10 '''.format(work_dir, len(model["classes"]))
    
    if model["network"]["input"]["type"] == "image":
        cfg_options += " \\\n    height={} \\\n    width={}".format(height, width)
    if dataset_url != "":
        cfg_options += " \\\n    data_root={}/dataset/".format(work_dir)
    if pretrain_url != "":
        cfg_options += " \\\n    load_from={}/pretrain.pth".format(work_dir)
    if config.get("argument", "") != "":
        cfg_options += " \\\n    {}".format(config.get("argument", ""))

    # Train Model 
    if config != "":
        notebook['cells'][9]['source'] = "!sscma.train {} \\\n{}".format(config_file, cfg_options)

        # Export Model
        notebook['cells'][11]['source'] = "import os\n"
        notebook['cells'][11]['source'] += "with open('{}/last_checkpoint', 'r') as f:\n\tos.environ['CHECKPOINT_FILE_PATH'] = f.read()".format(work_dir)
        notebook['cells'][12]['source'] = "!sscma.export {} $CHECKPOINT_FILE_PATH {}".format(config_file, cfg_options)
        notebook['cells'][15]['source'] = "!sscma.inference {} ${{CHECKPOINT_FILE_PATH%.*}}.pth \\\n{}".format(config_file, cfg_options)
        notebook['cells'][17]['source'] = "!sscma.inference {} ${{CHECKPOINT_FILE_PATH%.*}}_float32.onnx \\\n{}".format(config_file, cfg_options)
        notebook['cells'][19]['source'] = "!sscma.inference {} ${{CHECKPOINT_FILE_PATH%.*}}_float32.tflite \\\n{}".format(config_file, cfg_options)
        notebook['cells'][21]['source'] = "!sscma.inference {} ${{CHECKPOINT_FILE_PATH%.*}}_int8.tflite \\\n{}".format(config_file, cfg_options)
        notebook['cells'][23]['source'] = "%ls -lh {}/".format(work_dir)

    return notebook



def openai_reply(content, apikey):
    openai.api_key = apikey
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're an AI assistant who's good at translating English into Chinese."},
            {"role": "system", "content": 'Translate the following English nootbook to Chinese："{}"'.format(content)},
            ],
        temperature=0.5,
        max_tokens=2500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content

def generate():
    
    branch = get_current_branch()
    work_dir = os.getcwd()
    dist_dir = os.path.join(work_dir)
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
        
    sscma_model_data = '{"version": " 1", "models":[]}'
    sscma_model_json = json.loads(sscma_model_data)
    sscma_model_json["version"] = get_current_commit_hash()
    
    for file in find_files_in_folder("./", "json", exclude=["./", "./dist", "./.github", "./docs", "./notebooks", "./scripts", "./templates"]):
        print("Processing {}".format(file))
        with open(file, "r") as f:
            model = json.loads(f.read())
            sscma_model_json["models"].append(model)
            
            
            object_name = "{}_{}_{}".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_'), model["network"]["input"]["shape"][0])
            
            doc_en_dir = os.path.join(dist_dir, "docs/en")
            if not os.path.exists(doc_en_dir):
                os.makedirs(doc_en_dir) 
           
            #generate doc 
            doc_en_path = os.path.join(doc_en_dir, "{}.md".format(object_name))
            doc_en = generate_doc_en(model)
            if not os.path.exists(os.path.dirname(doc_en_path)):
                os.makedirs(os.path.dirname(doc_en_path))
            with open(os.path.join(doc_en_path), "w") as f:
                f.write(doc_en)
                
                
            doc_zh_CN_dir = os.path.join(dist_dir, "docs/zh_CN")
            if not os.path.exists(doc_zh_CN_dir):
                os.makedirs(doc_zh_CN_dir) 
                
            doc_zh_CN_path = os.path.join(doc_zh_CN_dir, "{}.md".format(object_name))
            doc_zh_CN = generate_doc_zh_CN(model)
            if not os.path.exists(os.path.dirname(doc_zh_CN_path)):
                os.makedirs(os.path.dirname(doc_zh_CN_path))
            with open(os.path.join(doc_zh_CN_path), "w") as f:
                f.write(doc_zh_CN)
            
            # generate notebook
            notebook_en_dir = os.path.join(dist_dir, "notebooks/en")
            if not os.path.exists(notebook_en_dir):
                os.makedirs(notebook_en_dir)
            notebook_en_path = os.path.join(notebook_en_dir, "{}.ipynb".format(object_name))
            notebook_en = generate_notebook_en(model)
            if not os.path.exists(os.path.dirname(notebook_en_path)):
                os.makedirs(os.path.dirname(notebook_en_path))
            with open(os.path.join(notebook_en_path), "w") as f:
                nbf.write(notebook_en, f)
                
            notebook_zh_CN_dir = os.path.join(dist_dir, "notebooks/zh_CN")
            if not os.path.exists(notebook_zh_CN_dir):
                os.makedirs(notebook_zh_CN_dir)
            notebook_zh_CN_path = os.path.join(notebook_zh_CN_dir, "{}.ipynb".format(object_name))
            notebook_zh_CN = generate_notebook_zh_CN(model)
            if not os.path.exists(os.path.dirname(notebook_zh_CN_path)):
                os.makedirs(os.path.dirname(notebook_zh_CN_path))
            with open(os.path.join(notebook_zh_CN_path), "w") as f:
                nbf.write(notebook_zh_CN, f)
            
    
    with open(os.path.join(dist_dir, "models.json"), "w") as f:
        json.dump(sscma_model_json, f, indent=4)
        
    # generate README.md
    model_list_en = ""
    model_list_zh_CN = ""
    
    categories = []
    for model in sscma_model_json["models"]:
        if model["category"] not in categories:
            categories.append(model["category"])
    
    for category in categories:
        model_list_en += "### {}\n\n".format(category)
        header_en = ["Model", "Colab"]
        table_en = []
        model_list_zh_CN += "### {}\n\n".format(category)
        header_zh_CN = ["模型", "Colab"]
        table_zh_CN = []
        for model in sscma_model_json["models"]:
            if model["category"] == category:
                object_name = "{}_{}_{}".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_'), model["network"]["input"]["shape"][0])
                table_en.append(["[{}]({})".format(object_name, "docs/en/{}.md".format(object_name)), "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/{}/notebooks/en/{}.ipynb)".format(branch,object_name)])
                table_zh_CN.append(["[{}]({})".format(object_name, "docs/zh_CN/{}.md".format(object_name)), "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/{}/notebooks/zh_CN/{}.ipynb)".format(branch,object_name)])
        model_list_en += tabulate(table_en, header_en, tablefmt="pipe", numalign="center", stralign="left") + "\n\n"
        model_list_zh_CN += tabulate(table_zh_CN, header_zh_CN, tablefmt="pipe", numalign="center", stralign="left") + "\n\n"
    
    with open(os.path.join(work_dir, "templates", "README.template.en.md"), "r") as file:
        readme_en = file.read()
    
        readme_en = readme_en.replace("{{model_list}}", model_list_en)
    
        with open(os.path.join(dist_dir, "README.md"), "w") as f:
            f.write(readme_en)
            
    
    with open(os.path.join(work_dir, "templates", "README.template.zh_CN.md"), "r") as file:
        readme_zh_CN = file.read()
        print()
        readme_zh_CN = readme_zh_CN.replace("{{model_list}}", model_list_zh_CN)
    
        with open(os.path.join(dist_dir, "README_zh_CN.md"), "w") as f:
            f.write(readme_zh_CN)
    
    
def check():
    for file in find_files_in_folder("./", "json", exclude=["./", "./dist", "./.github", "./docs", "./notebooks", "./scripts", "./templates"]):
        print("check {}".format(file))
        with open(file, "r") as f:
            model = json.loads(f.read())
            if check_json(model) == False:
                raise ValueError("Invalid models.json file - {}".format(file))

def download():
    base_folder = "model_zoo"  # Replace with the actual base folder
    for file in find_files_in_folder("./", "json", exclude=["./", "./dist", "./.github", "./docs", "./notebooks", "./scripts", "./templates"]):
        with open(file, "r") as f:
            model = json.loads(f.read())
            for item in model["benchmark"]:
                url = item["url"]
                sub_path = os.path.dirname(file)  # Get the subpath relative to the base folder
                download_folder = os.path.join(base_folder, sub_path)
                if not os.path.exists(download_folder):
                    os.makedirs(download_folder)
                
                file_path = download_file(url, download_folder)
                item["checksum"] = get_file_md5(file_path)
            model["uuid"] = "0000"
            model["uuid"] = hashlib.md5(json.dumps(model).encode()).hexdigest()
            
        json.dump(model, open(file, "w"), indent=4) 

            
def main():
    parser = argparse.ArgumentParser(description='SSCMA Model Zoo')
    parser.add_argument('-g', '--generate', action='store_true', help='Generate Model Zoo')
    parser.add_argument('-c', '--check', action='store_true', help='Check Model Zoo')
    parser.add_argument('-d', '--download', action='store_true', help='Download Model Zoo')
    parser.add_argument('--apikey', type=str, help='OpenAI API Key')
    args = parser.parse_args()
    
    if args.check:
        check()
    
    if args.download:
        download()
        
    if args.generate:
        generate()
        

   
if __name__ == "__main__":
    main()