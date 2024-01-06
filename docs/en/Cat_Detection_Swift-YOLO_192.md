# Cat Detection - Swift-YOLO

English | [简体中文](../zh_CN/Cat_Detection_Swift-YOLO_192.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/Cat_Detection_Swift-YOLO_192.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/swift_yolo/swift_yolo_tiny_1xb16_300e_coco.py)

**Dataset:** [Cat](https://universe.roboflow.com/animal-cegrr/cat-x8ov4/dataset/1)

**Class:** `cat`

![Cat Detection](https://files.seeedstudio.com/sscma/static/detection_cat.png)

The model is a Swift-YOLO model trained on the cat detection dataset.

### Network 

|        | Type   |  Batch  | Shape         | Remark                                                                                                           |
|:-------|:-------|:-------:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| Output | bbox   |    1    | [2268, 6]     | The output is a 2268x6 tensor, where 2268 is the number of candidate boxes and 6 is [x, y, w, h, score, [class]] |
### Benchmark

|   Backend    |  Precision  |  mAP(%)  |  Flops(M)  |  Params(M)  |    Inference(ms)    |                                              Download                                              |    Author    |
|:------------:|:-----------:|:--------:|:----------:|:-----------:|:-------------------:|:--------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    |   FLOAT32   |  96.90   |   90.564   |    0.699    |          -          |       [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/cat/cat_detection.pth)        | Seeed Studio |
|     ONNX     |   FLOAT32   |  92.60   |     -      |    0.699    |          -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/cat/cat_detection_float32.onnx)   | Seeed Studio |
|    TFLite    |   FLOAT32   |  92.60   |     -      |      -      |          -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/cat/cat_detection_float32.tflite)  | Seeed Studio |
|    TFLite    |    INT8     |  92.70   |     -      |      -      | 625.0<sup>(1)</sup> |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/cat/cat_detection_int8.tflite)    | Seeed Studio |
| TFLite(vela) |    INT8     |  92.70   |     -      |      -      |  45<sup>(2)</sup>   | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/cat/cat_detection_int8_vela.tflite) | Seeed Studio |

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

