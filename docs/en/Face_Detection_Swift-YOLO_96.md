# Face Detection - Swift-YOLO

English | [简体中文](../zh_CN/Face_Detection_Swift-YOLO_96.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/Face_Detection_Swift-YOLO_96.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/swift_yolo/swift_yolo_tiny_1xb16_300e_coco.py)

**Dataset:** [face detection](https://universe.roboflow.com/detection-02p2y/face-b3jhr/dataset/2)

**Class:** `face`

![Face Detection](https://files.seeedstudio.com/sscma/static/detection_face.png)

The model is a Swift-YOLO model trained on the face detection dataset.

### Network 

|        | Type   |  Batch  | Shape       | Remark                                                                                                         |
|:-------|:-------|:-------:|:------------|:---------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [96, 96, 3] | The input image should be resized to 96x96 pixels.                                                             |
| Output | bbox   |    1    | [567, 6]    | The output is a 567x6 tensor, where 567 is the number of candidate boxes and 6 is [x, y, w, h, score, [class]] |
### Benchmark

|   Backend    |  Precision  |  mAP(%)  |  Flops(M)  |  Params(M)  |    Inference(ms)    |                                                                                   Download                                                                                   |    Author    |
|:------------:|:-----------:|:--------:|:----------:|:-----------:|:-------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    |   FLOAT32   |  98.70   |   22.641   |    0.699    |          -          |       [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/face_detection/swift_yolo_1xb16_300e_coco_300_sha1_fe1d7dec30d62e583a7ccf717fd6585c792570bf.pth)        | Seeed Studio |
|     ONNX     |   FLOAT32   |  97.90   |     -      |    0.699    |          -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/face_detection/swift_yolo_1xb16_300e_coco_300_float32_sha1_441e4868e17a9bac5740280b3db791a6d75ac8a7.onnx)   | Seeed Studio |
|    TFLite    |   FLOAT32   |  97.90   |     -      |      -      |          -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/face_detection/swift_yolo_1xb16_300e_coco_300_float32_sha1_7c75dc6e777e3d3098d7f0bdb3e5c529c4d2865a.tflite)  | Seeed Studio |
|    TFLite    |    INT8     |  97.90   |     -      |      -      | 180.0<sup>(1)</sup> |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/face_detection/swift_yolo_1xb16_300e_coco_300_int8_sha1_2287b951101007d4cd1d09c3da68e53e6f23a071.tflite)    | Seeed Studio |
| TFLite(vela) |    INT8     |  97.90   |     -      |      -      |  33<sup>(2)</sup>   | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/face_detection/swift_yolo_1xb16_300e_coco_300_int8_sha1_2287b951101007d4cd1d09c3da68e53e6f23a071_vela.tflite) | Seeed Studio |

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

