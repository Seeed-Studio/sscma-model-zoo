
### Face Detection

![Face Detection](https://cdn.jsdelivr.net/gh/Seeed-Studio/sscma-model-zoo@main/detection/assets/images/face_detection.png)

- **YOLOv5**

| Model Name  | Backend | Input Size | Precision  | mAP| MACs (M) | Param (M) | Invoking RAM (M) | Invoke Time (ms) | Link  |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| YOLOv5 Tiny | PyTorch | 192x192x3  | Float32    | 94.4%   | 90.56   | 0.67|-|-| [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_sha1_f2a3f61a271c467748e26f0fd6fdd82d740512ff.pth)  |
| YOLOv5 Tiny | ONNX    | 192x192x3  | Float32    | 94.0% | - | 0.67| - | - | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_sha1_e530c8df4b4474979cbfe2da447d06ab657289ce.onnx) |
| YOLOv5 Tiny | TFLite  | 192x192x3  | Float32    | 94.0%           | 89.00    | - | 1.20| - | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_float32_sha1_a647ee0f7eb8951b3d78c8048159e999029d7051.tflite) |
| YOLOv5 Tiny | TFlite  | 192x192x3  | Int8 (PTQ) | 93.1% | 89.00 | - |0.35 | 671.24<sup>(2)</sup>/890.83<sup>(3)</sup>  893.62<sup>(4)</sup> | [Download](https://github.com/Seeed-Studio/sscma-model-zoo/raw/dev/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_int8_sha1_e707d23e1b45b4a464e9ebedae0f6570a9d35a9c.tflite)|
| YOLOv5 Tiny | onnx  | 96\*96\*3 | float32 | 86.5% | 22.641 | 0.699  | -| - | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_96x96_float32_sha1_ba3a6a7de5bea92eb702a863608b64b70c04f79b.onnx)    |
| YOLOv5 Tiny | TFlite  | 96\*96\*3 | float32 | 86.5% | 22.641 | 0.699  | -| - | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_96x96_float32_sha1_5a4b846ea88784bc275367ae8c371ba0e4916f9b.tflite)    |
| YOLOv5 Tiny | TFlite  | 96\*96\*3 | Int8 (PTQ) | 82.9% | 22.641 | 0.699  | -| 201<sup>(1) | [Download](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_96x96_int8_sha1_ec2821e32f70f816872a384c1e4cf3a635a38954.tflite)    |
