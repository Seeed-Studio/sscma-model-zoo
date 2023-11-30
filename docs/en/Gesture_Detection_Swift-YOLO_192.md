# Gesture Detection - Swift-YOLO

English | [简体中文](../zh_CN/Gesture_Detection_Swift-YOLO_192.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/Gesture_Detection_Swift-YOLO_192.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](configs/yolov5/swift_yolo_1xb16_300e_coco.py)

**Dataset:** [Gesture](https://app.roboflow.com/rsp/paper-aaj0p/33)

**Class:** `paper`, `rock`, `scissors`

![Gesture Detection](https://files.seeedstudio.com/sscma/static/detection_gesture.png)

The model is a Swift-YOLO model trained on the gesture detection dataset.

### Network 

|        | Type   |  Batch  | Shape         | Remark                                                                                                           |
|:-------|:-------|:-------:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| Output | bbox   |    1    | [2268, 8]     | The output is a 2268x8 tensor, where 2268 is the number of candidate boxes and 8 is [x, y, w, h, score, [class]] |
### Benchmark

|  Backend  |  Precision  |  mAP(%)  |  Flops(M)  |  Params(M)  |    Inference(ms)    |                                                                                 Download                                                                                  |    Author    |
|:---------:|:-----------:|:--------:|:----------:|:-----------:|:-------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|  PyTorch  |   FLOAT32   |  90.60   |    90.8    |     0.7     |          -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/swift-yolo/gesture/swift_yolo_1xb16_300e_coco_sha1_adda465db843aae8384c90c82e223c2cd931cad2.pth)   | Seeed Studio |
|   ONNX    |   FLOAT32   |  91.90   |     -      |     0.7     |          -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/swift-yolo/gesture/swift_yolo_1xb16_300e_coco_sha1_6f0e8c8ad5a6eb5c9afb5f18f43063dcc065c4b8.onnx)  | Seeed Studio |
|  TFLite   |   FLOAT32   |  91.90   |     -      |      -      |          -          | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/swift-yolo/gesture/swift_yolo_1xb16_300e_coco_sha1_54f794c25b545a1d33502e3f93a620c4cecfb1f9.tflite) | Seeed Studio |
|  TFLite   |    INT8     |  93.00   |     -      |      -      | 642.0<sup>(1)</sup> | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/swift-yolo/gesture/swift_yolo_1xb16_300e_coco_sha1_8d25b2b0be2a0ea38d3fe0aca5ce3891f7aa67c5.tflite) | Seeed Studio |

***Table Notes:***

- ***Evaluation Parameters:**  Confidence Threshold: 0.001, IoU Threshold: 0.55, mAP Eval IoU: 0.50..*
- ***Backend:** The deep learning framework used to infer the model.*
- ***Precision:** The numerical precision used for training the model.*
- ***Metrics:** The metrics used to evaluate the model.*
- ***Inference(ms):** The inference time of the model in milliseconds.*
  - ***1:** xiao_esp32s3.*
- ***Link:** The link to the model.*
- ***Author:** The author of the model.*

### License

MIT

