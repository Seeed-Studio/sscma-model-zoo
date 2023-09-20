# Person Classification - MobileNetV2(0.35) Rep

[English](../en/Person_Classification_MobileNetV2(0.35)_Rep_64.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/refactor-auto-generate/notebooks/zh_CN/Person_Classification_MobileNetV2(0.35)_Rep_64.ipynb)

**版本：** 1.0.0

**类别：** Image Classification

**算法：** [MobileNetV2(0.35) Rep](https://raw.githubusercontent.com/Seeed-Studio/SSCMA/main/configs/classification/mobnetv2_0.35_rep_1bx16_300e_custom.py)

**数据集：** [VWW](https://github.com/Mxbonn/visualwakewords)

**类别：** `Not a person`, `Person`

![Person Classification](https://files.seeedstudio.com/sscma/static/person_cls.png)

The model is a vision model designed for CIFAR-10 classification. It utilizes the [SSCMA](https://github.com/Seeed-Studio/SSCMA) training and employs the MobileNetV2 (0.35) Rep algorithm.

### 网络架构

|      | 类型           |  批次  | 形状        | 备注                                                                                                          |
|:-----|:---------------|:------:|:------------|:--------------------------------------------------------------------------------------------------------------|
| 输入 | image          |   1    | [64, 64, 3] | The input image should be resized to 32x32 pixels                                                             |
| 输出 | classification |   1    | [2]         | The output is a 2-element vector, which represents the probability of the input image belonging to each class |
### 基准测试

|  框架   |  精度   |  Top-1(%)  |  Flops(MB)  |  Params(MB)  |   Inference(ms)   |                                                                                   下载                                                                                    |     作者     |
|:-------:|:-------:|:----------:|:-----------:|:------------:|:-----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
| PyTorch | FLOAT32 |   85.22    |     34      |     2.71     |         -         |  [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/person/mobilenetv2_0.35rep_vww32_float32_sha1_c0bb3413912614cb90492eb4c2fbfbf6d3005874.pth)   | Seeed Studio |
|  ONNX   | FLOAT32 |   80.33    |      -      |     2.71     |         -         |  [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/person/mobilenetv2_0.35rep_vww32_float32_sha1_1cf8b63ca70b701385f0fc15294593dd356ad60f.onnx)  | Seeed Studio |
| TFLite  | FLOAT32 |   80.34    |      -      |     2.71     |         -         | [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/person/mobilenetv2_0.35rep_vww32_float32_sha1_5231d2f72ff1668e202cf80d7735e8878f706cda.tflite) | Seeed Studio |
| TFLite  |  INT8   |   80.23    |      -      |     0.02     | 101<sup>(1)</sup> |  [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/person/mobilenetv2_0.35rep_vww32_int8_sha1_a90a9f8f09ac45022ced9ded3ab84790e5b35e59.tflite)   | Seeed Studio |

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

