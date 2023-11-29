# Gender Classification - MobileNetV2 0.35 Rep

[English](../en/Gender_Classification_MobileNetV2_0.35_Rep_64.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Gender_Classification_MobileNetV2_0.35_Rep_64.ipynb)

**版本：** 1.0.0

**任务** Image Classification

**算法：** [MobileNetV2 0.35 Rep](configs/classification/mobnetv2_0.35_rep_1bx16_300e_custom.py)

**数据集：** [Gender](https://universe.roboflow.com/seeed-studio-e2fso/gender-8vbxd)

**类别** `Not a person`, `Person`

![Gender Classification](https://files.seeedstudio.com/sscma/static/gender_cls.png)

The model is a vision model designed for Gender classification. It utilizes the [SSCMA](https://github.com/Seeed-Studio/SSCMA) training and employs the MobileNetV2 (0.35) Rep algorithm.

### 网络架构

|      | 类型           |  批次  | 形状        | 备注                                                                                                          |
|:-----|:---------------|:------:|:------------|:--------------------------------------------------------------------------------------------------------------|
| 输入 | image          |   1    | [64, 64, 3] | The input image should be resized to 64x64 pixels                                                             |
| 输出 | classification |   1    | [2]         | The output is a 2-element vector, which represents the probability of the input image belonging to each class |
### 基准测试

|  框架   |  精度   |  Top-1(%)  |  Flops(M)  |  Params(M)  |  Inference(ms)   |                                                                            下载                                                                            |     作者     |
|:-------:|:-------:|:----------:|:----------:|:-----------:|:----------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
| PyTorch | FLOAT32 |   94.50    |    5.49    |    2.16     |        -         |     [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/gender/mbv2_0.35_rep_gender_sha1_62336a001f0cd58d2ac8ed5a6823b9ac7374f276.pth)     | Seeed Studio |
|  ONNX   | FLOAT32 |   94.50    |     -      |    2.16     |        -         |       [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/gender/mbv2_0.35_rep_gender_a9031151303fb4eaeae99262d26c0719a7bca7d7.onnx)       | Seeed Studio |
| TFLite  | FLOAT32 |   94.50    |     -      |    2.16     |        -         |      [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/gender/mbv2_0.35_rep_gender_5e6dc80bd5f3ddb429326a27f767816d998c919b.tflite)      | Seeed Studio |
| TFLite  |  INT8   |   94.30    |     -      |    2.16     | 40<sup>(1)</sup> | [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/gender/mbv2_0.35_rep_gender_int8_sha1_2bc5677615f8aeb41bffe21e25de6d01f91c3a41.tflite) | Seeed Studio |

***表格注释：***

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

