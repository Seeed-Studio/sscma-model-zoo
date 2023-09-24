# Face Detection - Swift-YOLO

English | [简体中文](../zh_CN/Face_Detection_Swift-YOLO_192.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/Face_Detection_Swift-YOLO_192.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](configs/yolov5/yolov5_tiny_1xb16_300e_coco.py)

**Dataset:** [Face](https://universe.roboflow.com/detection-kgpie/face-detection-j0igc)

**Class:** `Face`

![Face Detection](https://files.seeedstudio.com/sscma/static/detection_face.png)

The model is a Swift-YOLO model trained on the Face dataset. The model can detect faces in images.

### Network 

|        | Type   |  Batch  | Shape         | Remark                                                                                                           |
|:-------|:-------|:-------:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| Output | bbox   |    1    | [2268, 5]     | The output is a 2268x5 tensor, where 2268 is the number of candidate boxes and 5 is [x, y, w, h, score, [class]] |
### Benchmark

|  Backend  |  Precision  |  mAP(%)  |  MACs(MB)  |  Params(M)  |  Peek RAM(MB)  |               Inference(ms)                |                                                                                  Download                                                                                   |    Author    |
|:---------:|:-----------:|:--------:|:----------:|:-----------:|:--------------:|:------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|  PyTorch  |   FLOAT32   |  94.40   |   90.56    |    0.67     |       -        |                     -                      |      [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_sha1_f2a3f61a271c467748e26f0fd6fdd82d740512ff.pth)       | Seeed Studio |
|   ONNX    |   FLOAT32   |  94.10   |     -      |    0.67     |       -        |                     -                      |      [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_sha1_e530c8df4b4474979cbfe2da447d06ab657289ce.onnx)      | Seeed Studio |
|  TFLite   |   FLOAT32   |  94.10   |    89.0    |      -      |      1.2       |                     -                      | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_float32_sha1_a647ee0f7eb8951b3d78c8048159e999029d7051.tflite) | Seeed Studio |
|  TFLite   |    INT8     |  93.10   |    89.0    |      -      |      0.35      | 790.0<sup>(1)</sup><br>691.0<sup>(2)</sup> |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_int8_sha1_e707d23e1b45b4a464e9ebedae0f6570a9d35a9c.tflite)   | Seeed Studio |

***Table Notes:***

- ***Evaluation Parameters:**  Confidence Threshold: 0.001, IoU Threshold: 0.55, mAP Eval IoU: 0.50..*
- ***Backend:** The deep learning framework used to infer the model.*
- ***Precision:** The numerical precision used for training the model.*
- ***Metrics:** The metrics used to evaluate the model.*
- ***Inference(ms):** The inference time of the model in milliseconds.*
  - ***1:** grove_vision_ai.*
  - ***2:** xiao_esp32s3.*
- ***Link:** The link to the model.*
- ***Author:** The author of the model.*

### License

MIT

