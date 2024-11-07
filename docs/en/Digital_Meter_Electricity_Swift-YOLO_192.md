# Digital Meter Electricity - Swift-YOLO

English | [简体中文](../zh_CN/Digital_Meter_Electricity_Swift-YOLO_192.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/Digital_Meter_Electricity_Swift-YOLO_192.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/swift_yolo/swift_yolo_tiny_1xb16_300e_coco.py)

**Dataset:** [Digital Meter Electricity](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-electricity)

**Class:** `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`

![Digital Meter Electricity](https://files.seeedstudio.com/sscma/static/detect_meter.png)

The model is a Swift-YOLO model trained on the Digital Meter Electricity dataset, which can detect the 7-segment digital meter.

### Network 

|        | Type   |  Batch  | Shape         | Remark                                                                                                             |
|:-------|:-------|:-------:|:--------------|:-------------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                               |
| Output | bbox   |    1    | [2268, 15]    | The output is a 2268x15 tensor, where 2268 is the number of candidate boxes and 15 is [x, y, w, h, score, [class]] |
### Benchmark

|   Backend    |  Precision  |  mAP(%)  |  MACs(MB)  |  Params(M)  |  Peek RAM(MB)  |    Inference(ms)    |                                                                                   Download                                                                                   |    Author    |
|:------------:|:-----------:|:--------:|:----------:|:-----------:|:--------------:|:-------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    |   FLOAT32   |  99.20   |   90.56    |    0.67     |       -        |          -          |       [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/electricity_meter/yolov5_tiny_1xb16_300e_coco_sha1_b26cffe14038a7155315c40b49f851679a547dec.pth)        | Seeed Studio |
|     ONNX     |   FLOAT32   |  98.80   |     -      |    0.67     |      1.2       |          -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/electricity_meter/yolov5_tiny_1xb16_300e_coco_float32_sha1_e46a4c7183d073a5807e327d6b6d788853f2acf7.tflite)  | Seeed Studio |
|    TFLite    |   FLOAT32   |  98.80   |    89.0    |      -      |      1.2       |          -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/electricity_meter/yolov5_tiny_1xb16_300e_coco_int8_sha1_d670a8f8ceb3691beaa89da352c678634a29df73.tflite)    | Seeed Studio |
|    TFLite    |    INT8     |  93.10   |    89.0    |      -      |      0.35      | 691.0<sup>(1)</sup> |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/electricity_meter/yolov5_tiny_1xb16_300e_coco_int8_sha1_d670a8f8ceb3691beaa89da352c678634a29df73.tflite)    | Seeed Studio |
| TFLite(vela) |    INT8     |  93.10   |    89.0    |      -      |      0.35      |  50<sup>(2)</sup>   | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/electricity_meter/yolov5_tiny_1xb16_300e_coco_int8_sha1_d670a8f8ceb3691beaa89da352c678634a29df73_vela.tflite) | Seeed Studio |

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

