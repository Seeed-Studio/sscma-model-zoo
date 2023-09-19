import os
import json
import requests
import subprocess
import nbformat as nbf
from tabulate import tabulate

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

def generate_readme_zh_CN(model):
    
    readme = ""
    
    # 添加模型名称和描述
    readme += "# {} - {}\n\n".format(model["name"], model["algorithm"])
    
    # 添加Colab徽章
    readme += "[![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/SSCMA/notebooks/{}_{}.ipynb)\n\n".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_'))


    # 添加模型徽章
    readme += "**版本：** {}\n\n".format(model["version"])
    readme += "**类别：** {}\n\n".format(model["category"])
    readme += "**算法：** [{}]({})\n\n".format(model["algorithm"], model["config"])
    readme += "**数据集：** [{}]({})\n\n".format(model["dataset"]["name"], model["dataset"]["url"])

    # 添加类别
    readme += "**类别：** "
    readme += ", ".join(["`{}`".format(c) for c in model["classes"]]) + "\n\n"

    # 添加模型图片
    readme += "![{}]({})\n\n".format(model["name"], model["image"])
        
    # 添加模型描述
    readme += model["description"] + "\n\n"
    
    # 添加网络架构
    readme += "### 网络架构\n\n"
    network = model["network"]
    network_headers = ["", "类型", "批次大小", "形状", "备注"]
    network_table = []
    network_table.append(["输入", network["input"]["type"], network["batch"], network["input"]["shape"], network["input"].get("remark", "")])   
    network_table.append(["输出", network["output"]["type"], network["batch"], network["output"]["shape"], network["output"].get("remark", "")])
    readme += tabulate(network_table, network_headers, tablefmt="pipe") + "\n"
        
    # 添加基准测试
    readme += "### 基准测试\n\n"
    benchmark_headers = ["后端", "精度"]
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
                    benchmark_table[-1].append("<br>".join([str("{}<sup>({})</sup>".format(metrics[key].get(k, "-"), inference.index(k)+1)) for k in inference]))
                else:
                    benchmark_table[-1].append(metrics[key])
            else:
                benchmark_table[-1].append("-") 
                    
        benchmark_table[-1].append(link)
        benchmark_table[-1].append(author)
            
    readme += tabulate(benchmark_table, benchmark_headers, tablefmt="pipe", numalign="center", stralign="center") + "\n"
        
    # 添加表格注释
    readme += "\n"
    readme += "***表格注释：***\n\n"
    if "benchmark_note" in model:
        for key, value in model["benchmark_note"].items():
            readme += "- ***{}：*** {}.*\n".format(key, value)
    readme += "- ***后端：*** 用于推断模型的深度学习框架.*\n"
    readme += "- ***精度：*** 用于训练模型的数值精度.*\n"
    readme += "- ***指标：*** 用于评估模型的指标.*\n"
    readme += "- ***推理时间（毫秒）：*** 模型的推理时间（以毫秒为单位）.*\n"
    for i, key in enumerate(inference):
        readme += "  - ***{}：*** {}.*\n".format(i+1, key)
    readme += "- ***链接：*** 模型的链接.*\n"
    readme += "- ***作者：*** 模型的作者.*\n"
    readme += "\n"
        
    # 添加使用指南
    readme += "## 使用指南\n\n"
    if model.get("guidelines", "") != "":
        readme += model.get("guidelines", "")
    else:
        readme += "### 训练\n\n"
        readme += "使用以下参数训练模型：\n\n"
        readme += '```bash\n'
        readme += 'sscma.train {}\n'.format(model["config"])
        readme += '```\n\n'
        readme += "### 导出\n\n"
        readme += "使用以下参数导出模型：\n\n"
        readme += '```bash\n'
        readme += 'sscma.export {}\n'.format(model["config"])
        readme += '```\n\n'
        readme += "### 评估\n\n"
        readme += "使用以下参数评估模型：\n\n"
        readme += '```bash\n'
        readme += 'sscma.infernece {}\n'.format(model["config"])
        readme += '```\n\n'
    readme += "\n\n"
        
    # 添加许可证
    readme += "### 许可证\n\n"
    readme += model.get("license", "")
    readme += "\n\n"
        
    return readme

def generate_readme_en(model):
    
    readme = ""
    
    # Add model name and description
    readme += "# {} - {}\n\n".format(model["name"], model["algorithm"])
    
    # Add Colab Badge
    readme += "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/SSCMA/notebooks/{}_{}.ipynb)\n\n".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_'))


    # Add model badges
    readme += "**Version:** {}\n\n".format(model["version"])
    readme += "**Category:** {}\n\n".format(model["category"])
    readme += "**Algorithm:** [{}]({})\n\n".format(model["algorithm"], model["config"])
    readme += "**Dataset:** [{}]({})\n\n".format(model["dataset"]["name"], model["dataset"]["url"])

    # Add class
    readme += "**Class:** "
    readme += ", ".join(["`{}`".format(c) for c in model["classes"]]) + "\n\n"

    # Add model image
    readme += "![{}]({})\n\n".format(model["name"], model["image"])
        
    #Add model description
    readme += model["description"] + "\n\n"
    
    # Add Network Architecture
    readme += "### Network \n\n"
    network = model["network"]
    network_headers = ["", "Type", "Batch", "Shape", "Remark"]
    network_table = []
    network_table.append(["Input", network["input"]["type"], network["batch"], network["input"]["shape"], network["input"].get("remark", "")])   
    network_table.append(["Output", network["output"]["type"], network["batch"], network["output"]["shape"], network["output"].get("remark", "")])
    readme += tabulate(network_table, network_headers, tablefmt="pipe") + "\n"
        
    # Add Benchmark benchmark_table
    readme += "### Benchmark\n\n"
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
                    benchmark_table[-1].append("<br>".join([str("{}<sup>({})</sup>".format(metrics[key].get(k, "-"), inference.index(k)+1)) for k in inference]))
                else:
                    benchmark_table[-1].append(metrics[key])
            else:
                benchmark_table[-1].append("-") 
                    
        benchmark_table[-1].append(link)
        benchmark_table[-1].append(author)
            
    readme += tabulate(benchmark_table, benchmark_headers, tablefmt="pipe", numalign="center", stralign="center") + "\n"
        
    # Add Table Notes
    readme += "\n"
    readme += "***Table Notes:***\n\n"
    if "benchmark_note" in model:
        for key, value in model["benchmark_note"].items():
            readme += "- ***{}:** {}.*\n".format(key, value)
    readme += "- ***Backend:** The deep learning framework used to infer the model.*\n"
    readme += "- ***Precision:** The numerical precision used for training the model.*\n"
    readme += "- ***Metrics:** The metrics used to evaluate the model.*\n"
    readme += "- ***Inference(ms):** The inference time of the model in milliseconds.*\n"
    for i, key in enumerate(inference):
        readme += "  - ***{}:** {}.*\n".format(i+1, key)
    readme += "- ***Link:** The link to the model.*\n"
    readme += "- ***Author:** The author of the model.*\n"
    readme += "\n"
        
    # Add Guidelines
    readme += "## Guidelines\n\n"
    if model.get("guidelines", "") != "":
        readme += model.get("guidelines", "")
    else:
        readme += "### Training\n\n"
        readme += "The model was trained using the following parameters:\n\n"
        readme += '```bash\n'
        readme += 'sscma.train {}\n'.format(model["config"])
        readme += '```\n\n'
        readme += "### Exporting\n\n"
        readme += "The model was exported using the following parameters:\n\n"
        readme += '```bash\n'
        readme += 'sscma.export {}\n'.format(model["config"])
        readme += '```\n\n'
        readme += "### Evaluation\n\n"
        readme += "The model was evaluated using the following parameters:\n\n"
        readme += '```bash\n'
        readme += 'sscma.infernece {}\n'.format(model["config"])
        readme += '```\n\n'
    readme += "\n\n"
        
    # Add License
    readme += "### License\n\n"
    readme += model.get("license", "")
    readme += "\n\n"
        
    return readme

def generate_notebook_en(model):
    work_dir = os.getcwd()
    file = open(os.path.join(work_dir, "templates", "notebook.template.en.ipynb"))
    
    if file is None:
        raise ValueError("Invalid notebook template file")
    
    notebook = nbf.read(file, as_version=4)
    
    # Add model name and description
    content = ""
    content += "# {} - {}\n\n".format(model["name"], model["algorithm"])

    # Add model badges
    content += "**Version:** {}\n\n".format(model["version"])
    content += "**Category:** {}\n\n".format(model["category"])
    content += "**Algorithm:** [{}]({})\n\n".format(model["algorithm"], model["config"])
    content += "**Dataset:** [{}]({})\n\n".format(model["dataset"]["name"], model["dataset"]["url"])

    # Add class
    content += "**Class:** "
    content += ", ".join(["`{}`".format(c) for c in model["classes"]]) + "\n\n"

    # Add model image
    content += "![{}]({})\n\n".format(model["name"], model["image"])
        
    # Add model description
    content += model["description"] + "\n\n"
    
    notebook['cells'][2]['source'] = content
    
    # Train Model 
    notebook['cells'][10]['source'] = '!sscma.train {}'.format(model.get("config", "config.py"))
    
    # Export Model
    notebook['cells'][12]['source'] = '!sscma.export {}'.format(model.get("config", "config.py"))
    
    # Inference Model
    notebook['cells'][14]['source'] = '!sscma.inference {}'.format(model.get("config", "config.py")) 
    
                                                     
    # Export
    return notebook



def generate_notebook_zh_CN(model):
    work_dir = os.getcwd()
    file = open(os.path.join(work_dir, "templates", "notebook.template.zh_CN.ipynb"))
    
    if file is None:
        raise ValueError("Invalid notebook template file")
    
    notebook = nbf.read(file, as_version=4)
    
    # Add model name and description
    content = ""
    content += "# {} - {}\n\n".format(model["name"], model["algorithm"])

    # Add model badges
    content += "**版本:** {}\n\n".format(model["version"])
    content += "**类别:** {}\n\n".format(model["category"])
    content += "**算法:** [{}]({})\n\n".format(model["algorithm"], model["config"])
    content += "**数据集:** [{}]({})\n\n".format(model["dataset"]["name"], model["dataset"]["url"])

    # Add class
    content += "**Class:** "
    content += ", ".join(["`{}`".format(c) for c in model["classes"]]) + "\n\n"

    # Add model image
    content += "![{}]({})\n\n".format(model["name"], model["image"])
        
    # Add model description
    content += model["description"] + "\n\n"
    
    notebook['cells'][2]['source'] = content
    
    # Train Model 
    notebook['cells'][10]['source'] = '!sscma.train {}'.format(model.get("config", "config.py"))
    
    # Export Model
    notebook['cells'][12]['source'] = '!sscma.export {}'.format(model.get("config", "config.py"))
    
    # Inference Model
    notebook['cells'][14]['source'] = '!sscma.inference {}'.format(model.get("config", "config.py")) 
    
                                                     
    # Export
    return notebook

def main():
    
    work_dir = os.getcwd()
    dist_dir = os.path.join(work_dir, "dist")
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
        
    sscma_model_data = '{"version": " 1", "models":[]}'
    sscma_model_json = json.loads(sscma_model_data)
    sscma_model_json["version"] = get_current_commit_hash()
    
    for file in find_files_in_folder("./", "json", exclude=["./dist"]):
        print("Processing {}".format(file))
        with open(file, "r") as f:
            model = json.load(f)
            sscma_model_json["models"].append(model)
            # if check_json(model) == False:
            #     raise ValueError("Invalid models.json file - {}".format(file))
            doc_en_dir = os.path.join(dist_dir, "docs/en")
            if not os.path.exists(doc_en_dir):
                os.makedirs(doc_en_dir) 
            
            # generate readme 
            doc_en_path = os.path.join(doc_en_dir, os.path.dirname(file),  "{}_{}.md".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_')))
            readme_en = generate_readme_en(model)
            if not os.path.exists(os.path.dirname(doc_en_path)):
                os.makedirs(os.path.dirname(doc_en_path))
            with open(os.path.join(doc_en_path), "w") as f:
                f.write(readme_en)
                
                
            doc_zh_CN_dir = os.path.join(dist_dir, "docs/zh_CN")
            if not os.path.exists(doc_zh_CN_dir):
                os.makedirs(doc_zh_CN_dir) 
                
            doc_zh_CN_path = os.path.join(doc_zh_CN_dir, os.path.dirname(file),  "{}_{}.md".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_')))
            readme_zh_CN = generate_readme_zh_CN(model)
            if not os.path.exists(os.path.dirname(doc_zh_CN_path)):
                os.makedirs(os.path.dirname(doc_zh_CN_path))
            with open(os.path.join(doc_zh_CN_path), "w") as f:
                f.write(readme_zh_CN)
            
            # generate notebook
            notebook_en_dir = os.path.join(dist_dir, "notebooks/en")
            if not os.path.exists(notebook_en_dir):
                os.makedirs(notebook_en_dir)
            notebook_en_path = os.path.join(notebook_en_dir, os.path.dirname(file), "{}_{}.ipynb".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_')))
            notebook_en = generate_notebook_en(model)
            if not os.path.exists(os.path.dirname(notebook_en_path)):
                os.makedirs(os.path.dirname(notebook_en_path))
            with open(os.path.join(notebook_en_path), "w") as f:
                nbf.write(notebook_en, f)
                
            notebook_zh_CN_dir = os.path.join(dist_dir, "notebooks/zh_CN")
            if not os.path.exists(notebook_zh_CN_dir):
                os.makedirs(notebook_zh_CN_dir)
            notebook_zh_CN_path = os.path.join(notebook_zh_CN_dir, os.path.dirname(file), "{}_{}.ipynb".format(model["name"].replace(' ', '_'), model["algorithm"].replace(' ', '_')))
            notebook_zh_CN = generate_notebook_zh_CN(model)
            if not os.path.exists(os.path.dirname(notebook_zh_CN_path)):
                os.makedirs(os.path.dirname(notebook_zh_CN_path))
            with open(os.path.join(notebook_zh_CN_path), "w") as f:
                nbf.write(notebook_zh_CN, f)
            
    
    with open(os.path.join(dist_dir, "models.json"), "w") as f:
        json.dump(sscma_model_json, f, indent=4)

if __name__ == "__main__":
    main()