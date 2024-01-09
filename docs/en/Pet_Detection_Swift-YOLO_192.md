# Pet Detection - Swift-YOLO

English | [简体中文](../zh_CN/Pet_Detection_Swift-YOLO_192.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/Pet_Detection_Swift-YOLO_192.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/swift_yolo/swift_yolo_tiny_1xb16_300e_coco.py)

**Dataset:** [Animal](https://universe.roboflow.com/animal-cegrr/animal-ph37i/dataset/11)

**Class:** `cat`, `dog`

![Pet Detection](https://files.seeedstudio.com/sscma/static/detection_animal.png)

The model is a Swift-YOLO model trained on the animal detection dataset for cat and dog.

### Network 

|        | Type   |  Batch  | Shape         | Remark                                                                                                           |
|:-------|:-------|:-------:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| Output | bbox   |    1    | [2268, 7]     | The output is a 2268x7 tensor, where 2268 is the number of candidate boxes and 7 is [x, y, w, h, score, [class]] |
### Benchmark

|   Backend    |  Precision  |  mAP(%)  |  Flops(M)  |  Params(M)  |    Inference(ms)    |                                                 Download                                                 |    Author    |
|:------------:|:-----------:|:--------:|:----------:|:-----------:|:-------------------:|:--------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    |   FLOAT32   |  93.30   |   90.685   |     0.7     |          -          |       [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/animal/animal_detection.pth)        | Seeed Studio |
|     ONNX     |   FLOAT32   |  88.30   |     -      |     0.7     |          -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/animal/animal_detection_float32.onnx)   | Seeed Studio |
|    TFLite    |   FLOAT32   |  88.30   |     -      |      -      |          -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/animal/animal_detection_float32.tflite)  | Seeed Studio |
|    TFLite    |    INT8     |  87.10   |     -      |      -      | 706.0<sup>(1)</sup> |   [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/animal/animal_detection_int8.tflite)    | Seeed Studio |
| TFLite(vela) |    INT8     |  87.10   |     -      |      -      |  45<sup>(2)</sup>   | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/animal/animal_detection_int8_vela.tflite) | Seeed Studio |

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

