import argparse
import hashlib
import os
import sys

from loguru import logger
from termcolor import colored


def get_model_paths(paths: list, ignore_hidden=True):
    dirs = []
    models = []
    for path in paths:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if ignore_hidden and item.startswith("."):
                continue
            if os.path.isdir(item_path):
                dirs.append(item_path)
            elif os.path.splitext(item)[1] in [".pth", ".onnx", ".tflite"]:
                models.append(item_path)
    return models + get_model_paths(dirs, ignore_hidden) if len(dirs) != 0 else models


def verify_models(root: os.path):
    cwd = os.getcwd()
    models = get_model_paths([os.path.join(cwd, root)])
    bad_models = []
    if os.name == "nt":  # colored print patch on Windows (nt)
        os.system("color")
    print("Verifying SHA1 hashes of models:")
    for model in models:
        name = os.path.basename(model)
        sha1 = str(name).split("_sha1_")[1].split(".")[0]
        with open(model, "rb") as file:
            model_bytes = file.read()
            file_sha1 = hashlib.sha1(model_bytes).hexdigest()
        if file_sha1 != sha1:
            bad_models.append(model)
        print(" - ", name, ":", sep="")
        print(
            "\tStatus:",
            colored("Error", "red")
            if len(bad_models) != 0
            else colored("Passed", "green"),
        )
        print(
            "\tModel SHA1:",
            colored(file_sha1, "red" if len(bad_models) != 0 else "green"),
        )
        print("\tModel directory:", os.path.dirname(model))
    print("Verify results:")
    print("\tModels count:", len(models))
    print("\tVerify failed count:", len(bad_models))

    return 1 if len(bad_models) != 0 else 0


@logger.catch
def main():
    parser = argparse.ArgumentParser(description="Verify models")
    parser.add_argument(
        "--root", default="", help="root of edgelab-model-zoo repository"
    )
    args = parser.parse_args()

    ret = verify_models(args.root)
    sys.exit(ret)


if __name__ == "__main__":
    main()
