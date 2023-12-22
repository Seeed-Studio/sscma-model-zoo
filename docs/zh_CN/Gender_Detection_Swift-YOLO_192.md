# Gender Detection - Swift-YOLO

[English](../en/Gender_Detection_Swift-YOLO_192.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Gender_Detection_Swift-YOLO_192.ipynb)

**版本：** 1.0.0

**任务** Object Detection

**算法：** [Swift-YOLO](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/yolov5/swift_yolo_1xb16_300e_coco.py)

**数据集：** [Gender](https://universe.roboflow.com/aaa-61999/gender-ymxim/dataset/6)

**类别** `male`, `female`

![Gender Detection](https://files.seeedstudio.com/sscma/static/gender_cls.png)

The model is a Swift-YOLO model trained on the gender detection dataset.

### 网络架构

|    | 类型    |  批次  | 形状            | 备注                                                                                                               |
|:---|:------|:----:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| 输入 | image |  1   | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| 输出 | bbox  |  1   | [2268, 7]     | The output is a 2268x7 tensor, where 2268 is the number of candidate boxes and 7 is [x, y, w, h, score, [class]] |
### 基准测试

|      框架      |   精度    |  mAP(%)  |  Flops(M)  |  Params(M)  |    Inference(ms)    |                                                   下载                                                   |      作者      |
|:------------:|:-------:|:--------:|:----------:|:-----------:|:-------------------:|:------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    | FLOAT32 |  98.20   |   90.685   |     0.7     |          -          |       [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/gender/gender_detection.pth)        | Seeed Studio |
|     ONNX     | FLOAT32 |  95.60   |     -      |     0.7     |          -          |   [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/gender/gender_detection_float32.onnx)   | Seeed Studio |
|    TFLite    | FLOAT32 |  95.60   |     -      |      -      |          -          |  [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/gender/gender_detection_float32.tflite)  | Seeed Studio |
|    TFLite    |  INT8   |  95.50   |     -      |      -      | 631.0<sup>(1)</sup> |   [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/gender/gender_detection_int8.tflite)    | Seeed Studio |
| TFLite(vela) |  INT8   |  95.50   |     -      |      -      |  45<sup>(2)</sup>   | [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/gender/gender_detection_int8_vela.tflite) | Seeed Studio |

***表格注释：***

- ***Evaluation Parameters：***  Confidence Threshold: 0.001, IoU Threshold: 0.55, mAP Eval IoU: 0.50..*
- ***框架：** 用于推断模型的深度学习框架.*
- ***精度：** 用于训练模型的数值精度.*
- ***指标：** 用于评估模型的指标.*
- ***推理时间（毫秒）：** 模型的推理时间（以毫秒为单位）.*
  - ***1：** xiao_esp32s3.*
  - ***2：** grove_vision_ai_we2.*
- ***链接：** 模型的链接.*
- ***作者：** 模型的作者.*

## 使用指南

### 许可证

MIT

