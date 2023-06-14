# Detection Overview

The object detection model zoo includs several pre-trained models from different optimized neural networks which trained using [EdgeLab](https://github.com/Seeed-Studio/EdgeLab).

The hierarchy of detection directory is as follows:

```txt
detection
├── configs
|   └── ...
├── models
│   ├── <network name>
│   │   ├── <datasets name>
│   │   │   ├── <pre-trained model>
│   │   │   └── ...
│   │   └── ...
│   └── ...
└── ...
```

The `models` folder includes different neural networks, each neural network is denoted as its name, located on `<network name>` folder. Inside the neural network folder, the model may trained on different datasets, so we use the `<datasets name>` to to partition these pre-trained models into different folders.

Additionally, the `configs` folder stores the train configs, its directory hierarchy is as same as models.


## Performance of Models

The section summarizes the performance of different models trained from different neural networks.


### FOMO

| Model Name | Backend | Datasets | Input Size | Precision | F1 | FLOPs (M) | Parameters (M) | Invoking RAM (KiB) | Invoke Time* (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|--|
| FOMO MobileNetv2 | PyTorch | COCO_Person | 96x96x3 | float32 | 69.0% | 7.00 | 0.40 | - | - | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_8efbba3dacd06a3ac5636fbed215358a501ed1b1.pth) |
| FOMO MobileNetv2 | ONNX | COCO_Person | 96x96x3 | float32 | - | - | - | - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_sha1_ae595ad0271e084dbd8b584ad7f71b1646d13d36.onnx) |
| FOMO MobileNetv2 | TFLite | COCO_Person | 96x96x3 | int8 | - | - | - | - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_int8_sha1_b6f29c7486ed3d9cf6d64a5eb19ca3bd7328f25e.tflite) |

\**Invoke Time Measured on [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/).*


### YOLOv5

| Model Name | Backend | Datasets | Input Size | Precision | mAP* | FLOPs (M) | Parameters (M) | Invoking RAM (KiB) | Invoke Time* (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|--|
| YOLOv5 Tiny | PyTorch | COCO_Person | 192x192x3 | float32 | 45.8% | 90.56 | 0.67 | - | - | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_8efbba3dacd06a3ac5636fbed215358a501ed1b1.pth) |
| YOLOv5 Tiny | ONNX | COCO_Person | 192x192x3 | float32 | 45.8% | - | 0.67 | - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_cdb8b099a610d01b6e54715a76ef9757a2f86ffb.onnx) |
| YOLOv5 Tiny | TFLite | COCO_Person | 192x192x3 | int8 | 25.4% | - | - | 352.48 | 893.62 | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_int8_sha1_470cfb358b30c5aa97def1a5fdf178312f0d07c9.tflite) |

\**Confidence Threshold: `0.001`, IoU Threshold: `0.55`, mAP Eval IoU: `0.50`, Invoke Time Measured on [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/).*
