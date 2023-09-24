# Gender Detection - Swift-YOLO

English | [简体中文](../zh_CN/Gender_Detection_Swift-YOLO_96.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/Gender_Detection_Swift-YOLO_96.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](configs/yolov5/yolov5_tiny_1xb16_300e_coco.py)

**Dataset:** [Face Gender](https://universe.roboflow.com/seeed-studio-esmjg/person-detection-eetev)

**Class:** `Female`, `Male`

![Gender Detection](https://files.seeedstudio.com/sscma/static/gender_cls.png)

The model is a Swift-YOLO model trained on the face gender dataset. It can detect female and male faces in images.

### Network 

|        | Type   |  Batch  | Shape       | Remark                                                                                                         |
|:-------|:-------|:-------:|:------------|:---------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [96, 96, 3] | The input image should be resized to 96x96 pixels.                                                             |
| Output | bbox   |    1    | [567, 5]    | The output is a 567x5 tensor, where 567 is the number of candidate boxes and 5 is [x, y, w, h, score, [class]] |
### Benchmark

|  Backend  |  Precision  |  mAP(%)  |  Flops(M)  |  Params(M)  |  Peek RAM(MB)  |    Inference(ms)    |                                                                               Download                                                                               |    Author    |
|:---------:|:-----------:|:--------:|:----------:|:-----------:|:--------------:|:-------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|  PyTorch  |   FLOAT32   |  98.20   |    22.6    |     0.7     |       -        |          -          |      [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/gender/swift-yolo_tiny_gender_96_sha1_9d62ea47febade3f95cde715588b0e98377cd2f5.pth)       | Seeed Studio |
|   ONNX    |   FLOAT32   |  94.90   |     -      |     0.7     |       -        |          -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/gender/swift-yolo_tiny_gender_96_float32_sha1_16032922c6531011b1bfdbb2468415211c6dfc85.onnx)  | Seeed Studio |
|  TFLite   |   FLOAT32   |  94.90   |     -      |      -      |      1.2       |          -          | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/gender/swift-yolo_tiny_gender_96_float32_sha1_dfee634f289c9a7ad692c8bd558bdb3212756a4c.tflite) | Seeed Studio |
|  TFLite   |    INT8     |  94.90   |     -      |      -      |      0.35      | 200.0<sup>(1)</sup> |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/gender/swift-yolo_tiny_gender_96_int8_sha1_8078326f275ce87a371bbb273b010f9dce93f1c0.tflite)   | Seeed Studio |

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

