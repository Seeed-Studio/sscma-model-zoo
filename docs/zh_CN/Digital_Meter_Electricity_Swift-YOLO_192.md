# Digital Meter Electricity - Swift-YOLO

[English](../en/Digital_Meter_Electricity_Swift-YOLO_192.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/refactor-auto-generate/notebooks/zh_CN/Digital_Meter_Electricity_Swift-YOLO_192.ipynb)

**版本：** 1.0.0

**任务** Object Detection

**算法：** [Swift-YOLO](configs/yolov5/yolov5_tiny_1xb16_300e_coco.py)

**数据集：** [Digital Meter Electricity](https://universe.roboflow.com/seeed-studio-dbk14/digital-meter-electricity)

**类别** `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`

![Digital Meter Electricity](https://files.seeedstudio.com/sscma/static/detect_meter.png)

The model is a Swift-YOLO model trained on the Digital Meter Electricity dataset, which can detect the 7-segment digital meter.

### 网络架构

|      | 类型   |  批次  | 形状          | 备注                                                                                                             |
|:-----|:-------|:------:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| 输入 | image  |   1    | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| 输出 | bbox   |   1    | [2268, 5]     | The output is a 2268x5 tensor, where 2268 is the number of candidate boxes and 5 is [x, y, w, h, score, [class]] |
### 基准测试

|  框架   |  精度   |  mAP(%)  |  MACs(MB)  |  Params(M)  |  Peek RAM(MB)  |    Inference(ms)    |                                                                                           下载                                                                                            |     作者     |
|:-------:|:-------:|:--------:|:----------:|:-----------:|:--------------:|:-------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
| PyTorch | FLOAT32 |  99.20   |   90.56    |    0.67     |       -        |          -          |      [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_sha1_b26cffe14038a7155315c40b49f851679a547dec.pth)       | Seeed Studio |
|  ONNX   | FLOAT32 |  98.80   |     -      |    0.67     |      1.2       |          -          | [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_float32_sha1_e46a4c7183d073a5807e327d6b6d788853f2acf7.tflite) | Seeed Studio |
| TFLite  | FLOAT32 |  98.80   |    89.0    |      -      |      1.2       |          -          |  [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_int8_sha1_d670a8f8ceb3691beaa89da352c678634a29df73.tflite)   | Seeed Studio |
| TFLite  |  INT8   |  93.10   |    89.0    |      -      |      0.35      | 691.0<sup>(1)</sup> |  [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Digital_Meter_Seg7/yolov5_tiny_1xb16_300e_coco_int8_sha1_d670a8f8ceb3691beaa89da352c678634a29df73.tflite)   | Seeed Studio |

***表格注释：***

- ***Evaluation Parameters：***  Confidence Threshold: 0.001, IoU Threshold: 0.55, mAP Eval IoU: 0.50..*
- ***框架：** 用于推断模型的深度学习框架.*
- ***精度：** 用于训练模型的数值精度.*
- ***指标：** 用于评估模型的指标.*
- ***推理时间（毫秒）：** 模型的推理时间（以毫秒为单位）.*
  - ***1：** xiao_esp32s3.*
- ***链接：** 模型的链接.*
- ***作者：** 模型的作者.*

## 使用指南

### 许可证

MIT

