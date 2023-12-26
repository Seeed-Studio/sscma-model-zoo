# Gender Detection - Swift-YOLO

English | [简体中文](../zh_CN/Gender_Detection_Swift-YOLO_192.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/Gender_Detection_Swift-YOLO_192.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/swift_yolo/swift_yolo_tiny_1xb16_300e_coco.py)

**Dataset:** [Gender](https://universe.roboflow.com/aaa-61999/gender-ymxim/dataset/6)

**Class:** `male`, `female`

![Gender Detection](https://files.seeedstudio.com/sscma/static/gender_cls.png)

The model is a Swift-YOLO model trained on the gender detection dataset.

### Network 

|        | Type   |  Batch  | Shape         | Remark                                                                                                           |
|:-------|:-------|:-------:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| Output | bbox   |    1    | [2268, 7]     | The output is a 2268x7 tensor, where 2268 is the number of candidate boxes and 7 is [x, y, w, h, score, [class]] |
### Benchmark

|   Backend    |  Precision  |  mAP(%)  |  Flops(M)  |  Params(M)  |    Inference(ms)    |                                                 Download                                                 |    Author    |
|:------------:|:-----------:|:--------:|:----------:|:-----------:|:-------------------:|:--------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    |   FLOAT32   |  98.20   |   90.685   |     0.7     |          -          |       [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/gender/gender_detection.pth)        | Seeed Studio |
|     ONNX     |   FLOAT32   |  95.60   |     -      |     0.7     |          -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/gender/gender_detection_float32.onnx)   | Seeed Studio |
|    TFLite    |   FLOAT32   |  95.60   |     -      |      -      |          -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/gender/gender_detection_float32.tflite)  | Seeed Studio |
|    TFLite    |    INT8     |  95.50   |     -      |      -      | 631.0<sup>(1)</sup> |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/gender/gender_detection_int8.tflite)    | Seeed Studio |
| TFLite(vela) |    INT8     |  95.50   |     -      |      -      |  45<sup>(2)</sup>   | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/gender/gender_detection_int8_vela.tflite) | Seeed Studio |

***Table Notes:***

- ***Evaluation Parameters:**  Confidence Threshold: 0.001, IoU Threshold: 0.55, mAP Eval IoU: 0.50..*
- ***Backend:** The deep learning framework used to infer the model.*
- ***Precision:** The numerical precision used for training the model.*
- ***Metrics:** The metrics used to evaluate the model.*
- ***Inference(ms):** The inference time of the model in milliseconds.*
  - ***1:** xiao_esp32s3.*
  - ***2:** grove_vision_ai_we2.*
- ***Link:** The link to the model.*
- ***Author:** The author of the model.*

### License

MIT

