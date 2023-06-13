# Detection Overview

The object detection model zoo includs several pretrained models from different optimized neural networks which trained using [EdgeLab](https://github.com/Seeed-Studio/EdgeLab).

The hierarchy of detection directory is as follows:

```txt
detection
├── models
│   ├── <network name>
│   │   ├── <datasets name>
│   │   │   ├── <pretrained model>
│   │   │   ├── <train config>
│   │   │   └── ...
│   │   └── ...
│   └── ...
└── ...
```

The `models` folder includes different neural networks, each neural network is denoted as its name, located on `<network name>` folder. Inside the neural network folder, the model may trained on different datasets, so we use the `<datasets name>` to to partition these pretrained models into different folders.

## Performance of Models

The section summarizes the performance of different models trained from different neural networks.

| Model Name | Backend | Datasets | Input Size | Precision | mAP* | FLOPs (M) | Parameters (M) | Invoking RAM (KiB) | Invoke Time* (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|--|
| yolov5_tiny_1xb16_300e_coco | PyTorch | COCO(Person) | 192x192x3 | float32 | 45.8% | 90.56 | 0.67 | - | - | [Download(Seeed)]() |
| yolov5_tiny_1xb16_300e_coco | ONNX | COCO(Person) | 192x192x3 | float32 | 45.8% | - | 0.66 | - | - | [Download(GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO(Person)/yolov5_tiny_1xb16_300e_coco_sha1_cdb8b099a610d01b6e54715a76ef9757a2f86ffb.onnx) |
| yolov5_tiny_1xb16_300e_coco | TFLite | COCO(Person) | 192x192x3 | int8 | 25.4% | - | - | 352.48 | 893.62 | [Download(GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO(Person)/yolov5_tiny_1xb16_300e_coco_int8_sha1_470cfb358b30c5aa97def1a5fdf178312f0d07c9.tflite) |

\* Confidence Threshold: `0.001`, IoU Threshold: `0.55`, Invoke Time Measured on [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/).
