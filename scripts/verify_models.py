import argparse
import os


def get_model_paths(paths: list, ignore_hidden=True):
    dirs = []
    models=[]
    for path in paths:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if ignore_hidden and item.startswith('.'):
                continue
            if os.path.isdir(item_path):
                dirs.append(item_path)
            elif os.path.splitext(item)[1] in ['.pth', '.onnx', '.tflite']:
                models.append(item_path)
    return models + get_model_paths(dirs) if len(dirs) != 0 else models


def verify_models(root):
    cwd = os.getcwd()
    models = get_model_paths([os.path.join(cwd, root)])

    # TODO: support check models sha1sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Verify models')
    parser.add_argument('--root', default='', help='root of edgelab-model-zoo repository')
    args = parser.parse_args()

    verify_models(args.root)
