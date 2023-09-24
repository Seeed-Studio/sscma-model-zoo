# Gender Detection - Swift-YOLO

[English](../en/Gender_Detection_Swift-YOLO_96.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Gender_Detection_Swift-YOLO_96.ipynb)

**版本：** 1.0.0

**任务** Object Detection

**算法：** [Swift-YOLO](configs/yolov5/yolov5_tiny_1xb16_300e_coco.py)

**数据集：** [Face Gender](https://universe.roboflow.com/seeed-studio-esmjg/person-detection-eetev)

**类别** `Female`, `Male`

![Gender Detection](https://files.seeedstudio.com/sscma/static/gender_cls.png)

The model is a Swift-YOLO model trained on the face gender dataset. It can detect female and male faces in images.

### 网络架构

|      | 类型   |  批次  | 形状        | 备注                                                                                                           |
|:-----|:-------|:------:|:------------|:---------------------------------------------------------------------------------------------------------------|
| 输入 | image  |   1    | [96, 96, 3] | The input image should be resized to 96x96 pixels.                                                             |
| 输出 | bbox   |   1    | [567, 5]    | The output is a 567x5 tensor, where 567 is the number of candidate boxes and 5 is [x, y, w, h, score, [class]] |
### 基准测试

|  框架   |  精度   |  mAP(%)  |  Flops(M)  |  Params(M)  |  Peek RAM(MB)  |    Inference(ms)    |                                                                                 下载                                                                                 |     作者     |
|:-------:|:-------:|:--------:|:----------:|:-----------:|:--------------:|:-------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
| PyTorch | FLOAT32 |  98.20   |    22.6    |     0.7     |       -        |          -          |      [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/gender/swift-yolo_tiny_gender_96_sha1_9d62ea47febade3f95cde715588b0e98377cd2f5.pth)       | Seeed Studio |
|  ONNX   | FLOAT32 |  94.90   |     -      |     0.7     |       -        |          -          |  [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/gender/swift-yolo_tiny_gender_96_float32_sha1_16032922c6531011b1bfdbb2468415211c6dfc85.onnx)  | Seeed Studio |
| TFLite  | FLOAT32 |  94.90   |     -      |      -      |      1.2       |          -          | [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/gender/swift-yolo_tiny_gender_96_float32_sha1_dfee634f289c9a7ad692c8bd558bdb3212756a4c.tflite) | Seeed Studio |
| TFLite  |  INT8   |  94.90   |     -      |      -      |      0.35      | 200.0<sup>(1)</sup> |  [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/gender/swift-yolo_tiny_gender_96_int8_sha1_8078326f275ce87a371bbb273b010f9dce93f1c0.tflite)   | Seeed Studio |

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

