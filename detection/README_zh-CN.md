# 目标检测概述

目标检测 Model Zoo 包含多个使用不同神经网络的预训练模型，这些模型是在 [EdgeLab](https://github.com/Seeed-Studio/EdgeLab) 优化的神经网络上训练的。

目标检测模型目录的层次结构如下：

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

## 任务场景与模型性能

本节总结了由不同神经网络训练的不同模型的性能，这些模型针对各种任务场景在不同的数据集上训练。

### 行人检测

![Person Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/edgelab-model-zoo@main/detection/assets/images/person_detection.png)

- **FOMO**

|modelname|backend|Datasets|input size|precision|mAP|MACs|Parameters|RAM|Invoke Time (ms)|Link|
|:---------:|:-:|:-:|:-:|:--------:|:---------:|:---------:|:--:|:----:|:-----------:|:-:|
| FOMO MobileNetv2 | PyTorch | [COCO_Person](https://cocodataset.org/) | 96x96x3    | Float32    | 57.5% | 7.00     | 0.40           | -                  | -                                                           | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_sha1_22e95589616023d70e5671b27f0fc4906230aefe.pth)                |
| FOMO MobileNetv2 | ONNX    | [COCO_Person](https://cocodataset.org/) | 96x96x3    | Float32    | 57.5% | -        | -              | -                  | -                                                           | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_sha1_65a999fadc666c2f2eb843d37a256c104b2e72df.onnx)           |
| FOMO MobileNetv2 | TFLite  | [COCO_Person](https://cocodataset.org/) | 96x96x3    | Float32    | 57.5% | 6.20     | -              | 0.93               | -                                                           | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_float32_sha1_154f7f8ae469e196b6d2d920c6bb8552b75e6872.tflite) |
| FOMO MobileNetv2 | TFLite  | [COCO_Person](https://cocodataset.org/) | 96x96x3    | Int8 (PTQ) | 56.4% | 6.20     | -              | 0.24               | 65.72<sup>(2)</sup>/98.28<sup>(3)</sup>/99.10<sup>(4)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_int8_sha1_f71baa4b43310a9d1fa9b128dca15d3bf9c2a696.tflite)    |

- **YOLOv5**

|modelname|backend|Datasets|input size|precision|mAP|MACs|Parameters|RAM|Invoke Time (ms)|Link|
|:---------:|:-:|:-:|:-:|:--------:|:---------:|:---------:|:--:|:----:|:-----------:|:-:|
| YOLOv5 Tiny | PyTorch | [COCO_Person](https://cocodataset.org/) | 192x192x3  | Float32    | 45.8%           | 90.56    | 0.67           | -                  | -                                                              | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_8efbba3dacd06a3ac5636fbed215358a501ed1b1.pth)                |
| YOLOv5 Tiny | ONNX    | [COCO_Person](https://cocodataset.org/) | 192x192x3  | Float32    | 45.8%           | -        | 0.67           | -                  | -                                                              | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_cdb8b099a610d01b6e54715a76ef9757a2f86ffb.onnx)           |
| YOLOv5 Tiny | TFLite  | [COCO_Person](https://cocodataset.org/) | 192x192x3  | Float32    | 45.8%           | 89.00    | -              | 1.20               | -                                                              | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_float32_sha1_4ca1ba6b7c881cc8d4589462b22ee1fa5365d8f7.tflite) |
| YOLOv5 Tiny | TFLite  | [COCO_Person](https://cocodataset.org/) | 192x192x3  | Int8 (PTQ) | 35.0%           | 89.00    | -              | 0.35               | 671.24<sup>(2)</sup>/890.83<sup>(3)</sup>/893.62<sup>(4)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_int8_sha1_a39e1664b3cefcc31c9267e78594c7ee0cbacc64.tflite)    |

### 表计数字检测

![Digital Meter Number Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/edgelab-model-zoo@main/detection/assets/images/digital_meter_number_detection.png)

- **YOLOv5**

|modelname|backend|Datasets|input size|precision|mAP|MACs|Parameters|RAM|Invoke Time (ms)|Link|
|:---------:|:-:|:-:|:-:|:--------:|:---------:|:---------:|:--:|:----:|:-----------:|:-:|
| YOLOv5 Tiny | PyTorch | [Digital_Meter_Seg7](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-seg7) | 192x192x3  | Float32    | 99.2%           | 90.56    | 0.67           | -                  | -                                                              | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_sha1_b26cffe14038a7155315c40b49f851679a547dec.pth)                |
| YOLOv5 Tiny | ONNX    | [Digital_Meter_Seg7](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-seg7) | 192x192x3  | Float32    | 98.8%           | -        | 0.67           | -                  | -                                                              | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_sha1_fafffe6308842f1510fb6dd01293db4243edd678.onnx)           |
| YOLOv5 Tiny | TFLite  | [Digital_Meter_Seg7](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-seg7) | 192x192x3  | Float32    | 98.8%           | 89.00    | -              | 1.20               | -                                                              | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_float32_sha1_e46a4c7183d073a5807e327d6b6d788853f2acf7.tflite) |
| YOLOv5 Tiny | TFlite  | [Digital_Meter_Seg7](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-seg7) | 192x192x3  | Int8 (PTQ) | 98.1%           | 89.00    | -              | 0.35               | 671.24<sup>(2)</sup>/890.83<sup>(3)</sup>/893.62<sup>(4)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_int8_sha1_d670a8f8ceb3691beaa89da352c678634a29df73.tflite)    |

### 水表数字检测

![Water Meter Number Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/edgelab-model-zoo@main/detection/assets/images/water_meter_number_detection.png)

- **YOLOv5**

|modelname|backend|Datasets|input size|precision|mAP|MACs|Parameters|RAM|Invoke Time (ms)|Link|
|:---------:|:-:|:-:|:-:|:--------:|:---------:|:---------:|:--:|:----:|:-----------:|:-:|
| YOLOv5 Tiny | PyTorch | [Digital_Meter_Water](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-water) | 192x192x3  | Float32    | 95.3%           | 90.56    | 0.67           | -                  | -                                                              | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_sha1_e10d262518622edc50e0820b213581fc8d628e2b.pth)                |
| YOLOv5 Tiny | ONNX    | [Digital_Meter_Water](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-water) | 192x192x3  | Float32    | 91.8%           | -        | 0.67           | -                  | -                                                              | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_sha1_e4139097229c74d6d627a769e788374f7bd23e48.onnx)           |
| YOLOv5 Tiny | TFLite  | [Digital_Meter_Water](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-water) | 192x192x3  | Float32    | 91.8%           | 89.00    | -              | 1.20               | -                                                              | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_float32_sha1_d523dd19922ff4a3a53a0795222121317d01354d.tflite) |
| YOLOv5 Tiny | TFlite  | [Digital_Meter_Water](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-water) | 192x192x3  | Int8 (PTQ) | 88.3%           | 89.00    | -              | 0.35               | 671.24<sup>(2)</sup>/890.83<sup>(3)</sup>/893.62<sup>(4)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_int8_sha1_7975ab6a7d1daa26f61a2d364f82594834587bfe.tflite)    |

### 人脸检测

![Face Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/edgelab-model-zoo@main/detection/assets/images/face_detection.png)

- **YOLOv5**

|modelname|backend|input size|precision|mAP|MACs|Parameters|RAM|Invoke Time (ms)|Link|
|:---------:|:-:|:-:|:--------:|:---------:|:---------:|:--:|:----:|:-----------:|:-:|
| YOLOv5 Tiny | PyTorch | 192x192x3  | Float32    | 94.4%   | 90.56   | 0.67|-|-| [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_sha1_f2a3f61a271c467748e26f0fd6fdd82d740512ff.pth)  |
| YOLOv5 Tiny | ONNX    | 192x192x3  | Float32    | 94.0% | - | 0.67| - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_sha1_e530c8df4b4474979cbfe2da447d06ab657289ce.onnx) |
| YOLOv5 Tiny | TFLite  | 192x192x3  | Float32    | 94.0%           | 89.00    | - | 1.20| - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_float32_sha1_a647ee0f7eb8951b3d78c8048159e999029d7051.tflite) |
| YOLOv5 Tiny | TFlite  | 192x192x3  | Int8 (PTQ) | 93.1% | 89.00 | - |0.35 | 671.24<sup>(2)</sup>/890.83<sup>(3)</sup>/893.62<sup>(4)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_int8_sha1_e707d23e1b45b4a464e9ebedae0f6570a9d35a9c.tflite)|
| YOLOv5 Tiny | TFlite  | 96\*96\*3 | Int8 (PTQ) | 93.1% | 22.00 | -  | -| 200<sup>(2)</sup>/890.83<sup>(3)</sup>/893.62<sup>(4)</sup> | [Download (GitHub)]()    |
| YOLOv5 Tiny | onnx  | 96\*96\*3 | float32 | 86.5% | 22.641 | 0.699  | -| - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Face/yolov5_tiny_96x96_float32_sha1_ba3a6a7de5bea92eb702a863608b64b70c04f79b.onnx)    |
| YOLOv5 Tiny | TFlite  | 96\*96\*3 | float32 | 86.5% | 22.641 | 0.699  | -| - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Face/yolov5_tiny_96x96_float32_sha1_5a4b846ea88784bc275367ae8c371ba0e4916f9b.tflite)    |
| YOLOv5 Tiny | TFlite  | 96\*96\*3 | Int8 (PTQ) | 82.9% | 22.641 | 0.699  | -| 201<sup>(2) | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Face/yolov5_tiny_96x96_int8_sha1_20548b3a3c004b6a3a1169479dceb031586cb5c1.tflite)    |

<br></br>

*备注:*

<sup>1</sup> Confidence Threshold: `0.001`，IoU Threshold: `0.55`，mAP Eval IoU: `0.50`。

<sup>2</sup> 在 [ESP32-S3 (XIAO)](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/) 测试。

<sup>3</sup> 在 [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/) 测试。

<sup>4</sup> 在 [SenseCAP A1101](https://wiki.seeedstudio.com/SenseCAP-Vision-AI-Get-Started/) 测试。
