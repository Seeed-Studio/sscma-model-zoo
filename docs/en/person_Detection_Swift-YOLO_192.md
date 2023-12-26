# person Detection - Swift-YOLO

English | [简体中文](../zh_CN/person_Detection_Swift-YOLO_192.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/person_Detection_Swift-YOLO_192.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/swift_yolo/swift_yolo_shuff_1xb16_300e_coco.py)

**Dataset:** [](https://universe.roboflow.com/hanzhou-7mktt/ssperson/dataset/7)

**Class:** `person`

![person Detection](https://files.seeedstudio.com/sscma/static/detection_coco.png)

The model is a Swift-YOLO model trained on the person detection dataset.

### Network 

|        | Type   |  Batch  | Shape         | Remark                                                                                                           |
|:-------|:-------|:-------:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| Output | bbox   |    1    | [2268, 6]     | The output is a 2268x6 tensor, where 2268 is the number of candidate boxes and 6 is [x, y, w, h, score, [class]] |
### Benchmark

|   Backend    |  Precision  |  mAP(%)  |  Flops(M)  |  Params(M)  |  Peek RAM(MB)  |    Inference(ms)    |                                                                             Download                                                                              |    Author    |
|:------------:|:-----------:|:--------:|:----------:|:-----------:|:--------------:|:-------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    |   FLOAT32   |  95.40   |    194     |     0.7     |       -        |          -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/person/swift_yolo_shuffle_coco_320_float32_sha1_a5927bd6a6c6569d27edb98da946a8e75a8d816f.pth)    | Seeed Studio |
|     ONNX     |   FLOAT32   |  95.40   |     -      |     0.7     |       -        |          -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/person/swift_yolo_shuffle_coco_320_float32_sha1_20bc2c8517a8e42699bf46f1409f7541e52345ac.onnx)   | Seeed Studio |
|    TFLite    |   FLOAT32   |  95.40   |     -      |      -      |      1.2       |          -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/person/swift_yolo_shuffle_coco_320_float32_sha1_5dfa1a16d27ef347c0173c5297395963760fcc57.tflite)  | Seeed Studio |
|    TFLite    |    INT8     |  91.70   |     -      |      -      |      0.35      | 200.0<sup>(1)</sup> |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/person/swift_yolo_shuffle_coco_320_int8_sha1_3b0a6d7fd95e9dd21902beae6fa2d1cd0807bd7b.tflite)    | Seeed Studio |
| TFLite(vela) |    INT8     |  91.70   |     -      |      -      |      0.35      | 46.0<sup>(2)</sup>  | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/person/swift_yolo_shuffle_coco_320_int8_sha1_3b0a6d7fd95e9dd21902beae6fa2d1cd0807bd7b_vela.tflite) | Seeed Studio |

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

