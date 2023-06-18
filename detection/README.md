# Detection Overview

The object detection model zoo includs several pre-trained models from different optimized neural networks which trained using [EdgeLab](https://github.com/Seeed-Studio/EdgeLab).

The hierarchy of detection directory is as follows:

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

The `models` folder includes different neural networks, each neural network is denoted as its name, located on `<network name>` folder. Inside the neural network folder, the model may trained on different datasets, so we use the `<datasets name>` to to partition these pre-trained models into different folders.


## Performance of Models

The section summarizes the performance of different models trained from different neural networks.


### FOMO

| Model Name | Backend | Datasets | Input Size | Precision | F1 | MACs (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|--|
| FOMO MobileNetv2 | PyTorch | COCO_Person | 96x96x3 | Float32 | 69.0% | 7.00 | 0.40 | - | - | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_8efbba3dacd06a3ac5636fbed215358a501ed1b1.pth) |
| FOMO MobileNetv2 | ONNX | COCO_Person | 96x96x3 | Float32 | - | - | - | - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_sha1_ae595ad0271e084dbd8b584ad7f71b1646d13d36.onnx) |
| FOMO MobileNetv2 | TFLite | COCO_Person | 96x96x3 | Float32 | - | 6.20 | - | 0.93 | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_float32_sha1_fef54aa3d4b38b09cc38d01f9d14022cc178d5de.tflite) |
| FOMO MobileNetv2 | TFLite | COCO_Person | 96x96x3 | Int8 (PTQ) | - | 6.20 | - | 0.24 | 98.28<sup>(2)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_int8_sha1_b6f29c7486ed3d9cf6d64a5eb19ca3bd7328f25e.tflite) |



### YOLOv5

| Model Name | Backend | Datasets | Input Size | Precision | mAP<sup>*</sup> | MACs (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|--|
| YOLOv5 Tiny | PyTorch | COCO_Person | 192x192x3 | Float32 | 45.8% | 90.56 | 0.67 | - | - | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_8efbba3dacd06a3ac5636fbed215358a501ed1b1.pth) |
| YOLOv5 Tiny | ONNX | COCO_Person | 192x192x3 | Float32 | 45.8% | - | 0.67 | - | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_cdb8b099a610d01b6e54715a76ef9757a2f86ffb.onnx) |
| YOLOv5 Tiny | TFLite | COCO_Person | 192x192x3 | Float32 | 45.8% | 89.00 | - | 1.20 | - | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_float32_sha1_4ca1ba6b7c881cc8d4589462b22ee1fa5365d8f7.tflite) |
| YOLOv5 Tiny | TFLite | COCO_Person | 192x192x3 | Int8 (PTQ) | 35.0% | 89.00 | - | 0.35 | 893.62<sup>(2)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_int8_sha1_a39e1664b3cefcc31c9267e78594c7ee0cbacc64.tflite) |


## Exmaple of Models

The section shows the example of models trained from different datasets.

### FOMO

| Model Name | Backend | Datasets | Input Size | Precision | F1 | Link |
|--|--|--|--|--|--|--|
| FOMO MobileNetv2<sup>(1)(2)</sup>| TFLite | [face](TODO) | 96x96x3 | Float32 | 91.0% | [Download (Seeed Studio)](TODO) |


### YOLOv5

| Model Name | Backend | Datasets | Input Size | Precision | mAP<sup>*</sup> | Link |
|--|--|--|--|--|--|--|
| YOLOv5 Tiny<sup>(1)(2)</sup>| TFLite | [face](TODO) | 192x192x3 | Float32 | 92% | [Download (Seeed Studio)](TODO) |
｜ YOLOv5 Tiny<sup>(3)</sup> | TFLite | [digital meter](TODO) | 192x192x3 | Int8 (PTQ) | 90% | [Download (Seeed Studio)](TODO) |

## Notes
<sup>*</sup>*Confidence Threshold: `0.001`, IoU Threshold: `0.55`, mAP Eval IoU: `0.50`.* 

<sup>1</sup> *[ESP32-S3 (XIAO)](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/)* 

<sup>2</sup> *[Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/)*

<sup>3</sup> *[SenseCAP A1101](https://wiki.seeedstudio.com/SenseCAP-Vision-AI-Get-Started/)*