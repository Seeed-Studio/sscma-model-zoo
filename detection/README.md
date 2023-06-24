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


## Task Scanarios and Model Performance

The section summarizes the performance of various models trained from different neural networks using different datasets for diverse detection task scanarios.


### Person Detection

![Person Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/edgelab-model-zoo@dev/detection/assets/images/person_detection.png)


- **FOMO**

| Model Name       | Backend | Datasets                                | Input Size | Precision  | F1    | MACs (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms)    | Link                                                                                                                                                                                                         |
|------------------|---------|-----------------------------------------|------------|------------|-------|----------|----------------|--------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FOMO MobileNetv2 | PyTorch | [COCO_Person](https://cocodataset.org/) | 96x96x3    | Float32    | 69.0% | 7.00     | 0.40           | -                  | -                   | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_8efbba3dacd06a3ac5636fbed215358a501ed1b1.pth)                 |
| FOMO MobileNetv2 | ONNX    | [COCO_Person](https://cocodataset.org/) | 96x96x3    | Float32    | -     | -        | -              | -                  | -                   | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_sha1_ae595ad0271e084dbd8b584ad7f71b1646d13d36.onnx)           |
| FOMO MobileNetv2 | TFLite  | [COCO_Person](https://cocodataset.org/) | 96x96x3    | Float32    | -     | 6.20     | -              | 0.93               | -                   | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_float32_sha1_fef54aa3d4b38b09cc38d01f9d14022cc178d5de.tflite) |
| FOMO MobileNetv2 | TFLite  | [COCO_Person](https://cocodataset.org/) | 96x96x3    | Int8 (PTQ) | -     | 6.20     | -              | 0.24               | 98.28<sup>(3)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/fomo/COCO_Person/fomo_mobnetv2_0.35_x8_abl_coco_int8_sha1_b6f29c7486ed3d9cf6d64a5eb19ca3bd7328f25e.tflite)    |

- **YOLOv5**

| Model Name  | Backend | Datasets                                | Input Size | Precision  | mAP<sup>1</sup> | MACs (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms)     | Link                                                                                                                                                                                                        |
|-------------|---------|-----------------------------------------|------------|------------|-----------------|----------|----------------|--------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| YOLOv5 Tiny | PyTorch | [COCO_Person](https://cocodataset.org/) | 192x192x3  | Float32    | 45.8%           | 90.56    | 0.67           | -                  | -                    | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_8efbba3dacd06a3ac5636fbed215358a501ed1b1.pth)                |
| YOLOv5 Tiny | ONNX    | [COCO_Person](https://cocodataset.org/) | 192x192x3  | Float32    | 45.8%           | -        | 0.67           | -                  | -                    | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_sha1_cdb8b099a610d01b6e54715a76ef9757a2f86ffb.onnx)           |
| YOLOv5 Tiny | TFLite  | [COCO_Person](https://cocodataset.org/) | 192x192x3  | Float32    | 45.8%           | 89.00    | -              | 1.20               | -                    | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_float32_sha1_4ca1ba6b7c881cc8d4589462b22ee1fa5365d8f7.tflite) |
| YOLOv5 Tiny | TFLite  | [COCO_Person](https://cocodataset.org/) | 192x192x3  | Int8 (PTQ) | 35.0%           | 89.00    | -              | 0.35               | 893.62<sup>(3)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/COCO_Person/yolov5_tiny_1xb16_300e_coco_int8_sha1_a39e1664b3cefcc31c9267e78594c7ee0cbacc64.tflite)    |


### Digital Meter Number Detection

![Digital Meter Number Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/edgelab-model-zoo@dev/detection/assets/images/digital_meter_number_detection.png)


- **YOLOv5**

| Model Name  | Backend | Datasets                                                                                  | Input Size | Precision  | mAP<sup>1</sup> | MACs (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms)     | Link                                                                                                                                                                                                               |
|-------------|---------|-------------------------------------------------------------------------------------------|------------|------------|-----------------|----------|----------------|--------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| YOLOv5 Tiny | PyTorch | [Digital_Meter_Seg7](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-seg7) | 192x192x3  | Float32    | 99.2%           | 90.56    | 0.67           | -                  | -                    | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_sha1_b26cffe14038a7155315c40b49f851679a547dec.pth)                |
| YOLOv5 Tiny | ONNX    | [Digital_Meter_Seg7](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-seg7) | 192x192x3  | Float32    | 98.8%           | -        | 0.67           | -                  | -                    | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_sha1_fafffe6308842f1510fb6dd01293db4243edd678.onnx)           |
| YOLOv5 Tiny | TFLite  | [Digital_Meter_Seg7](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-seg7) | 192x192x3  | Float32    | 98.8%           | 89.00    | -              | 1.20               | -                    | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_float32_sha1_e46a4c7183d073a5807e327d6b6d788853f2acf7.tflite) |
| YOLOv5 Tiny | TFlite  | [Digital_Meter_Seg7](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-seg7) | 192x192x3  | Int8 (PTQ) | 98.1%           | 89.00    | -              | 0.35               | 893.62<sup>(4)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_int8_sha1_d670a8f8ceb3691beaa89da352c678634a29df73.tflite)    |


### Water Meter Number Detection

![Water Meter Number Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/edgelab-model-zoo@dev/detection/assets/images/water_meter_number_detection.png)


- **YOLOv5**

| Model Name  | Backend | Datasets                                                                                    | Input Size | Precision  | mAP<sup>1</sup> | MACs (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms)     | Link                                                                                                                                                                                                                |
|-------------|---------|---------------------------------------------------------------------------------------------|------------|------------|-----------------|----------|----------------|--------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| YOLOv5 Tiny | PyTorch | [Digital_Meter_Water](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-water) | 192x192x3  | Float32    | 95.3%           | 90.56    | 0.67           | -                  | -                    | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_sha1_e10d262518622edc50e0820b213581fc8d628e2b.pth)                |
| YOLOv5 Tiny | ONNX    | [Digital_Meter_Water](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-water) | 192x192x3  | Float32    | 91.8%           | -        | 0.67           | -                  | -                    | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_sha1_e4139097229c74d6d627a769e788374f7bd23e48.onnx)           |
| YOLOv5 Tiny | TFLite  | [Digital_Meter_Water](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-water) | 192x192x3  | Float32    | 91.8%           | 89.00    | -              | 1.20               | -                    | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_float32_sha1_d523dd19922ff4a3a53a0795222121317d01354d.tflite) |
| YOLOv5 Tiny | TFlite  | [Digital_Meter_Water](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-water) | 192x192x3  | Int8 (PTQ) | 88.3%           | 89.00    | -              | 0.35               | 893.62<sup>(4)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_int8_sha1_7975ab6a7d1daa26f61a2d364f82594834587bfe.tflite)    |


### Face Detection

![Face Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/edgelab-model-zoo@dev/detection/assets/images/face_detection.png)


- **YOLOv5**

| Model Name  | Backend | Datasets                                                                   | Input Size | Precision  | mAP<sup>1</sup> | MACs (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms)     | Link                                                                                                                                                                                                 |
|-------------|---------|----------------------------------------------------------------------------|------------|------------|-----------------|----------|----------------|--------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| YOLOv5 Tiny | PyTorch | [Face](https://universe.roboflow.com/detection-kgpie/face-detection-j0igc) | 192x192x3  | Float32    | 94.4%           | 90.56    | 0.67           | -                  | -                    | [Download (Seeed Studio)](https://files.seeedstudio.com/edgelab/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_sha1_f2a3f61a271c467748e26f0fd6fdd82d740512ff.pth)                |
| YOLOv5 Tiny | ONNX    | [Face](https://universe.roboflow.com/detection-kgpie/face-detection-j0igc) | 192x192x3  | Float32    | 94.0%           | -        | 0.67           | -                  | -                    | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_sha1_e530c8df4b4474979cbfe2da447d06ab657289ce.onnx)           |
| YOLOv5 Tiny | TFLite  | [Face](https://universe.roboflow.com/detection-kgpie/face-detection-j0igc) | 192x192x3  | Float32    | 94.0%           | 89.00    | -              | 1.20               | -                    | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_float32_sha1_a647ee0f7eb8951b3d78c8048159e999029d7051.tflite) |
| YOLOv5 Tiny | TFlite  | [Face](https://universe.roboflow.com/detection-kgpie/face-detection-j0igc) | 192x192x3  | Int8 (PTQ) | 93.1%           | 89.00    | -              | 0.35               | 893.62<sup>(4)</sup> | [Download (GitHub)](https://github.com/Seeed-Studio/edgelab-model-zoo/raw/dev/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_int8_sha1_e707d23e1b45b4a464e9ebedae0f6570a9d35a9c.tflite)    |

<br></br>

*Note:*

<sup>1</sup> Confidence Threshold: `0.001`, IoU Threshold: `0.55`, mAP Eval IoU: `0.50`.

<sup>2</sup> Measured on [ESP32-S3 (XIAO)](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/).

<sup>3</sup> Measured on [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/).

<sup>4</sup> Measured on [SenseCAP A1101](https://wiki.seeedstudio.com/SenseCAP-Vision-AI-Get-Started/).
