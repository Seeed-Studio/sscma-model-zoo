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

| Model Name | Backend | Datasets | Input Size | Precision | mAP* | FLOPs (M) | Parameters (M) | Invoking RAM (KiB) | Invoking Time* (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|--|
| yolov5_tiny_1xb16_300e_coco | PyTorch | COCO(Person) | 192x192x3 | float32 | 45.8% | 90.56 | 0.67 | - | - | [Download(Seeed)]() |
| yolov5_tiny_1xb16_300e_coco | ONNX | COCO(Person) | 192x192x3 | float32 | 45.8% | - | 0.66 | - | - | [Download(GitHub)]() |
| yolov5_tiny_1xb16_300e_coco | TFLite | COCO(Person) | 192x192x3 | int8 | 25.4% | - | - | 352.48 | 893.62 | [Download(GitHub)]() |



