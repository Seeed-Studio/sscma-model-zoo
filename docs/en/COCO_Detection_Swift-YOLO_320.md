# COCO Detection - Swift-YOLO

English | [简体中文](../zh_CN/COCO_Detection_Swift-YOLO_320.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/COCO_Detection_Swift-YOLO_320.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/yolov5/swift_yolo_shuff_1xb16_300e_coco.py)

**Dataset:** [COCO2017](https://public.roboflow.com/object-detection/microsoft-coco-subset)

**Class:** `person`

![COCO Detection](https://files.seeedstudio.com/sscma/static/detection_coco.png)

The model is a Swift-YOLO model trained on the COCO2017 dataset.

### Network 

|        | Type   |  Batch  | Shape         | Remark                                                                                                            |
|:-------|:-------|:-------:|:--------------|:------------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [320, 320, 3] | The input image should be resized to 320x320 pixels.                                                              |
| Output | bbox   |    1    | [6300, 85]    | The output is a 6300x85 tensor, where 6300 is the number of candidate boxes and 5 is [x, y, w, h, score, [class]] |
### Benchmark

|   Backend    |  Precision  |  mAP(%)  |  Flops(M)  |  Params(M)  |  Peek RAM(MB)  |    Inference(ms)    |                                                                            Download                                                                             |    Author    |
|:------------:|:-----------:|:--------:|:----------:|:-----------:|:--------------:|:-------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    |   FLOAT32   |  25.10   |    194     |    0.63     |       -        |          -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/coco/swift_yolo_shuffle_coco_320_float32_sha1_a5927bd6a6c6569d27edb98da946a8e75a8d816f.pth)    | Seeed Studio |
|     ONNX     |   FLOAT32   |  25.10   |     -      |    0.63     |       -        |          -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/coco/swift_yolo_shuffle_coco_320_float32_sha1_20bc2c8517a8e42699bf46f1409f7541e52345ac.onnx)   | Seeed Studio |
|    TFLite    |   FLOAT32   |  25.10   |     -      |      -      |      1.2       |          -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/coco/swift_yolo_shuffle_coco_320_float32_sha1_5dfa1a16d27ef347c0173c5297395963760fcc57.tflite)  | Seeed Studio |
|    TFLite    |    INT8     |  25.10   |     -      |      -      |      0.35      | 200.0<sup>(1)</sup> |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/coco/swift_yolo_shuffle_coco_320_int8_sha1_3b0a6d7fd95e9dd21902beae6fa2d1cd0807bd7b.tflite)    | Seeed Studio |
| TFLite(vela) |    INT8     |  25.10   |     -      |      -      |      0.35      | 20.0<sup>(2)</sup>  | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/coco/swift_yolo_shuffle_coco_320_int8_sha1_3b0a6d7fd95e9dd21902beae6fa2d1cd0807bd7b_vela.tflite) | Seeed Studio |

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

