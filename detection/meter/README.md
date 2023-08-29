
### Digital Meter Number Detection

[Digital_Meter_Seg7](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-seg7)

![Digital Meter Number Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/sscma-model-zoo@main/detection/assets/images/digital_meter_number_detection.png)

- **YOLOv5**

| Model Name | Backend | Input Size | Precision | mAP<sup>1</sup> | MACs (M) | Param (M) | Invoking RAM (MiB) | Invoke Time (ms) | Link |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| YOLOv5 Tiny | PyTorch |192x192x3  | Float32    | 99.2%           | 90.56    | 0.67           | -                  | -                                                              | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_sha1_b26cffe14038a7155315c40b49f851679a547dec.pth)                |
| YOLOv5 Tiny | ONNX    | 192x192x3  | Float32    | 98.8%           | -        | 0.67           | -                  | -                                                              | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_sha1_fafffe6308842f1510fb6dd01293db4243edd678.onnx)           |
| YOLOv5 Tiny | TFLite  |192x192x3  | Float32    | 98.8%           | 89.00    | -              | 1.20               | -                                                              | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_float32_sha1_e46a4c7183d073a5807e327d6b6d788853f2acf7.tflite) |
| YOLOv5 Tiny | TFlite  | 192x192x3  | Int8 (PTQ) | 98.1%           | 89.00    | -              | 0.35               | 671.24<sup>(2)</sup>/890.83<sup>(3)</sup>/893.62<sup>(4)</sup> | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_int8_sha1_d670a8f8ceb3691beaa89da352c678634a29df73.tflite)    |

### Water Meter Number Detection

## Datasets: [Digital_Meter_Water](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-water)

![Water Meter Number Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/sscma-model-zoo@main/detection/assets/images/water_meter_number_detection.png)

- **YOLOv5**

| Model Name | Backend |  Input Size | Precision | mAP<sup>1</sup> | MACs (M) | Param (M) | Invoking RAM (MiB)|Invoke Time (ms) | Link |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| YOLOv5 Tiny | PyTorch | 192x192x3  | Float32    | 95.3%  | 90.56 | 0.67  | -   | | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_sha1_e10d262518622edc50e0820b213581fc8d628e2b.pth)                |
| YOLOv5 Tiny | ONNX    |  192x192x3  | Float32    | 91.8%           | -        | 0.67           | -                  | -                                                              | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_sha1_e4139097229c74d6d627a769e788374f7bd23e48.onnx)           |
| YOLOv5 Tiny | TFLite  |192x192x3  | Float32    | 91.8%           | 89.00    | -              | 1.20               | -                                                              | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_float32_sha1_d523dd19922ff4a3a53a0795222121317d01354d.tflite) |
| YOLOv5 Tiny | TFlite  | 192x192x3  | Int8 (PTQ) | 88.3%           | 89.00    | -              | 0.35               | 671.24<sup>(2)</sup>890.83<sup>(3)</sup>  893.62<sup>(4)</sup> | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_int8_sha1_7975ab6a7d1daa26f61a2d364f82594834587bfe.tflite)    |
