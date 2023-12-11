# Person Classification - MobileNetV2 0.35 Rep

[English](../en/Person_Classification_MobileNetV2_0.35_Rep_96.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Person_Classification_MobileNetV2_0.35_Rep_96.ipynb)

**版本：** 1.0.0

**任务** Image Classification

**算法：** [MobileNetV2 0.35 Rep](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/classification/mobnetv2_0.35_rep_1bx16_300e_custom.py)

**数据集：** [VWW](https://github.com/Mxbonn/visualwakewords)

**类别** `Not a person`, `Person`

![Person Classification](https://files.seeedstudio.com/sscma/static/person_cls.png)

The model is a vision model designed for CIFAR-10 classification. It utilizes the [SSCMA](https://github.com/Seeed-Studio/SSCMA) training and employs the MobileNetV2 (0.35) Rep algorithm.

### 网络架构

|    | 类型             |  批次  | 形状          | 备注                                                                                                            |
|:---|:---------------|:----:|:------------|:--------------------------------------------------------------------------------------------------------------|
| 输入 | image          |  1   | [96, 96, 3] | The input image should be resized to 96x96 pixels                                                             |
| 输出 | classification |  1   | [2]         | The output is a 2-element vector, which represents the probability of the input image belonging to each class |
### 基准测试

|      框架      |   精度    |  Top-1(%)  |  Flops(MB)  |  Params(M)  |   Inference(ms)    |                                                                                 下载                                                                                 |      作者      |
|:------------:|:-------:|:----------:|:-----------:|:-----------:|:------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    | FLOAT32 |   88.37    |    76.5     |    2.71     |         -          |   [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww96_float32_sha1_0b47deccb4ffab4d8f970ea6379b838163e5bd8f.pth)    | Seeed Studio |
|     ONNX     | FLOAT32 |   88.36    |      -      |    2.71     |         -          |   [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww96_float32_sha1_689cbad95dc725880861e72b5b9f7878f04ce17f.onnx)   | Seeed Studio |
|    TFLite    | FLOAT32 |   88.36    |      -      |    2.71     |         -          |  [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww96_float32_sha1_a92eb1b9420f2947bfb65153e1def12097fdb977.tflite)  | Seeed Studio |
|    TFLite    |  INT8   |   88.27    |      -      |    2.71     | 582<sup>(1)</sup>  |   [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww96_int8_sha1_f1a66ce5a3f05bc1293920e5a95f547e27df6550.tflite)    | Seeed Studio |
| TFLite(vela) |  INT8   |   88.27    |      -      |    2.71     | 15.0<sup>(2)</sup> | [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww96_int8_sha1_f1a66ce5a3f05bc1293920e5a95f547e27df6550_vela.tflite) | Seeed Studio |

***表格注释：***

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

