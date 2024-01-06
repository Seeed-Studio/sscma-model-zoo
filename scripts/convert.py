import json
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input file')
    parser.add_argument('output', help='output file')
    parser.add_argument('--precision', help='precision', default='INT8')
    parser.add_argument('--backend', help='backend', default='TFLite')
    parser.add_argument('--device', help='device', default='esp32s3')
    args = parser.parse_args()

    with open(args.input) as f:
        data = json.load(f)
        
    print("Converting", args.input, "to", args.output)

    target = {}
    target['models'] = []

    for model in data['models']:
        t_model = {
            "uuid": next(item["checksum"] for item in model["benchmark"] if item["precision"] == args.precision and args.backend in item["backend"]).split(":")[1],
            "name": model["name"],
            "version": model["version"],
            "category": model["category"],
            "model_type": "TFLite",
            "algorithm": model["algorithm"],
            "description": model["description"],
            "image": model["image"],
            "classes": model["classes"],
            "devices": args.device,
            "url": next(item["url"] for item in model["benchmark"] if item["precision"] == args.precision and args.backend in item["backend"]),
            "metrics": next(item["metrics"] for item in model["benchmark"] if item["precision"] == args.precision and args.backend in item["backend"]),
            "author": next(item["author"] for item in model["benchmark"] if item["precision"] == args.precision and args.backend in item["backend"]),
            "checksum": next(item["checksum"] for item in model["benchmark"] if item["precision"] == args.precision and args.backend in item["backend"]),
            "license": model["license"]
        }
        target['models'].append(t_model)
    
    with open(args.output, 'w') as f:
        json.dump(target, f, indent=4)

if __name__ == "__main__":
    main()
