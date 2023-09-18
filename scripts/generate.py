import os
import json
import glob
import requests
from tabulate import tabulate
import subprocess

def get_current_commit_hash():
    try:
        # 运行Git命令获取当前commit hash
        result = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
        # 解码结果并移除空白字符
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
    

def generate_readme_en(model):
    
    readme = ""
    
    # Add model name and description
    readme += "# {} - {}\n\n".format(model["name"], model["algorithm"])

    # Add model badges
    readme += "**Version:** {}\n\n".format(model["version"])
    readme += "**Category:** {}\n\n".format(model["category"])
    readme += "**Algorithm:** [{}]({})\n\n".format(model["algorithm"], model["config"])
    readme += "**Dataset:** [{}]({})\n\n".format(model["dataset"]["name"], model["dataset"]["url"])

    # Add class
    readme += "**Class:** "
    readme += ", ".join(model["classes"]) + "\n\n"

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

def find_files_in_folder(folder_path, extension):
    files = []
    for root, dirs, filenames in os.walk(folder_path):
        for file in filenames:
            if file.endswith(f".{extension}"):
                files.append(os.path.join(root, file))
    return files

# def parse_args():
#     parser = argparse.ArgumentParser(description="Generate README.md")
#     parser.add_argument("--input", "-i", type=str, default="models.json", help="Path to models.json")
#     parser.add_argument("--output", "-o", type=str, default="./", help="Path to output README.md")
#     return parser.parse_args()

def main():
    #args = parse_args()
    
    # if not os.path.exists(args.input):
    #     raise FileNotFoundError("File not found: {}".format(args.input))
    
    
    work_dir = os.getcwd()
    dist_dir = os.path.join(work_dir, "dist")
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
        
    sscma_model_data = '{"version": " 1", "models":[]}'
    sscma_model_json = json.loads(sscma_model_data)
    sscma_model_json["version"] = get_current_commit_hash()
    
        
    for file in find_files_in_folder("./", "json"):
        with open(file, "r") as f:
            data = json.load(f)
            sscma_model_json["models"].append(data)
            # if check_json(data) == False:
            #     raise ValueError("Invalid models.json file - {}".format(file))
            readme_en_dir = os.path.join(dist_dir, "docs/en")
            if not os.path.exists(readme_en_dir):
                os.makedirs(readme_en_dir) 
            
            path = os.path.join(readme_en_dir, os.path.dirname(file), os.path.basename(file).replace(".json", ".md"))
            readme_en = generate_readme_en(data)
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            with open(os.path.join(path), "w") as f:
                f.write(readme_en)
    
    with open(os.path.join(dist_dir, "models.json"), "w") as f:
        json.dump(sscma_model_json, f, indent=4)

if __name__ == "__main__":
    main()