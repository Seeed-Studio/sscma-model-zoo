import argparse
import hashlib
import os

from loguru import logger
from termcolor import colored


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


def verify_models(root: os.path):
    cwd = os.getcwd()
    models = get_model_paths([os.path.join(cwd, root)])
    bad_models = []
    if os.name == 'nt': # Colored print patch on Windows
        os.system('color')
    print('Verifying SHA1 hashes of models:')
    for model in models:
        name = os.path.basename(model)
        sha1 = str(name).split('_sha1_')[1].split('.')[0]
        with open(model, 'rb') as f:
            model_bytes = f.read()
            file_sha1 = hashlib.sha1(model_bytes).hexdigest()
        if file_sha1 != sha1:
            bad_models.append(model)
            print(name, ':', sep='')
            print('\tStatus:', colored('Error', 'red'))
            print('\tModel SHA1:', colored(f'{file_sha1}', 'red'))
            print('\tModel path:', os.path.dirname(model))
        print(name, ':', sep='')
        print('\tStatus:', colored('Passed', 'green'))
        print('\tModel SHA1:', colored(f'{file_sha1}', 'green'))
        print('\tModel path:', os.path.dirname(model))
    print('Verify results:')
    print(f'\tModels count: {len(models)}')
    print(f'\tBad Models count: {len(bad_models)}')
    if len(bad_models) != 0:
        raise ValueError(f'{len(bad_models)} model(s) not passed the SHA1 verify')


@logger.catch
def main():
    parser = argparse.ArgumentParser(description='Verify models')
    parser.add_argument('--root', default='', help='root of edgelab-model-zoo repository')
    args = parser.parse_args()

    verify_models(args.root)


if __name__ == '__main__':
    main()
