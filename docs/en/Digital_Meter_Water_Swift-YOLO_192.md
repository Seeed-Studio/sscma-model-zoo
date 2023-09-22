# Digital Meter Water - Swift-YOLO

English | [简体中文](../zh_CN/Digital_Meter_Water_Swift-YOLO_192.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/refactor-auto-generate/notebooks/en/Digital_Meter_Water_Swift-YOLO_192.ipynb)

**Version:** 1.0.0

**Category:** Object Detection

**Algorithm:** [Swift-YOLO](configs/yolov5/yolov5_tiny_1xb16_300e_coco.py)

**Dataset:** [Digital Meter Electricity](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-water)

**Class:** `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `-`

![Digital Meter Water](https://files.seeedstudio.com/sscma/static/detect_meter.png)

The model is a Swift-YOLO model trained on the Digital Meter Water dataset, which can detect the water meter number.

### Network 

|        | Type   |  Batch  | Shape         | Remark                                                                                                           |
|:-------|:-------|:-------:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| Input  | image  |    1    | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| Output | bbox   |    1    | [2268, 5]     | The output is a 2268x5 tensor, where 2268 is the number of candidate boxes and 5 is [x, y, w, h, score, [class]] |
### Benchmark

|  Backend  |  Precision  |  mAP(%)  |  MACs(MB)  |  Params(M)  |  Peek RAM(MB)  |    Inference(ms)    |                                                                                          Download                                                                                          |    Author    |
|:---------:|:-----------:|:--------:|:----------:|:-----------:|:--------------:|:-------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|  PyTorch  |   FLOAT32   |  95.30   |    91.8    |    0.67     |       -        |          -          |      [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_sha1_e10d262518622edc50e0820b213581fc8d628e2b.pth)       | Seeed Studio |
|   ONNX    |   FLOAT32   |  91.80   |     -      |    0.67     |      1.2       |          -          |      [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_sha1_e4139097229c74d6d627a769e788374f7bd23e48.onnx)      | Seeed Studio |
|  TFLite   |   FLOAT32   |  91.80   |    89.0    |      -      |      1.2       |          -          | [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_float32_sha1_d523dd19922ff4a3a53a0795222121317d01354d.tflite) | Seeed Studio |
|  TFLite   |    INT8     |  88.30   |    89.0    |      -      |      0.35      | 691.0<sup>(1)</sup> |  [Link](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Water/yolov5_tiny_1xb16_300e_coco_int8_sha1_7975ab6a7d1daa26f61a2d364f82594834587bfe.tflite)   | Seeed Studio |

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

