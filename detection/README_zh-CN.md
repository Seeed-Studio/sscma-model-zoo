# Detection 概述

目标检测 Model Zoo 包含多个使用不同神经网络的预训练模型，这些模型是在 [EdgeLab](https://github.com/Seeed-Studio/EdgeLab) 优化的神经网络上训练的。

检测目录的层次结构如下：

```txt
detection
├── models
│   ├── <network name>
│   │   ├── <datasets name>
│   │   │   ├── <pre-trained model>
│   │   │   └── ...
│   │   └── ...
│   └── ...
└── ...
```

文件夹 `models` 包含不同神经网络的预训练模型，各模型以其神经网络的名称表示，位于 `<network name>` 文件夹内。在对应模型的神经网络文件夹内，模型可能在不同的数据集上进行训练，因此我们使用 `<datasets name>` 来将这些预训练模型以实际训练的数据集划分到不同的文件夹中。


## 模型性能

本节总结了由不同神经网络训练的不同模型的性能。


### FOMO

| Model Name | Backend | Datasets | Input Size | Precision | F1 | FLOPs (M) | Parameters (M) | Invoking RAM (KiB) | Invoke Time* (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|--|
| FOMO MobileNetv2 | PyTorch | COCO_Person | 96x96x3 | float32 | 69.0% | 7.00 | 0.40 | - | - | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_8efbba3dacd06a3ac5636fbed215358a501ed1b1.pth) |
| FOMO MobileNetv2 | ONNX | COCO_Person | 96x96x3 | float32 | - | - | - | - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_sha1_ae595ad0271e084dbd8b584ad7f71b1646d13d36.onnx) |
| FOMO MobileNetv2 | TFLite | COCO_Person | 96x96x3 | float32 | - | - | - | - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_float32_sha1_fef54aa3d4b38b09cc38d01f9d14022cc178d5de.tflite) |
| FOMO MobileNetv2 | TFLite | COCO_Person | 96x96x3 | int8 | - | - | - | - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_int8_sha1_b6f29c7486ed3d9cf6d64a5eb19ca3bd7328f25e.tflite) |

\**Invoke Time Measured on [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/).*


### YOLOv5

| Model Name | Backend | Datasets | Input Size | Precision | mAP* | FLOPs (M) | Parameters (M) | Invoking RAM (KiB) | Invoke Time* (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|--|
| YOLOv5 Tiny | PyTorch | COCO_Person | 192x192x3 | float32 | 45.8% | 90.56 | 0.67 | - | - | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_8efbba3dacd06a3ac5636fbed215358a501ed1b1.pth) |
| YOLOv5 Tiny | ONNX | COCO_Person | 192x192x3 | float32 | 45.8% | - | 0.67 | - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_cdb8b099a610d01b6e54715a76ef9757a2f86ffb.onnx) |
| YOLOv5 Tiny | TFLite | COCO_Person | 192x192x3 | float32 | 45.8% | - | - | - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_float32_sha1_4ca1ba6b7c881cc8d4589462b22ee1fa5365d8f7.tflite) |
| YOLOv5 Tiny | TFLite | COCO_Person | 192x192x3 | int8 | 35.0% | - | - | 352.48 | 893.62 | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_int8_sha1_a39e1664b3cefcc31c9267e78594c7ee0cbacc64.tflite) |

\**Confidence Threshold: `0.001`, IoU Threshold: `0.55`, mAP Eval IoU: `0.50`, Invoke Time Measured on [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/).*
