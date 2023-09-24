# CIFAR-10 Classification - MobileNetV2 0.35 Rep

[English](../en/CIFAR-10_Classification_MobileNetV2_0.35_Rep_32.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/refactor-auto-generate/notebooks/zh_CN/CIFAR-10_Classification_MobileNetV2_0.35_Rep_32.ipynb)

**版本：** 1.0.0

**任务** Image Classification

**算法：** [MobileNetV2 0.35 Rep](configs/classification/mobnetv2_0.35_rep_1bx16_300e_cifar10.py)

**数据集：** [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html)

**类别** `Airplane`, `Automobile`, `Bird`, `Cat`, `Deer`, `Dog`, `Frog`, `Horse`, `Ship`, `Truck`

![CIFAR-10 Classification](https://files.seeedstudio.com/sscma/static/cifar10_cls_0_35.png)

The model is a vision model designed for CIFAR-10 classification. It utilizes the [SSCMA](https://github.com/Seeed-Studio/SSCMA) training and employs the MobileNetV2 (0.35) Rep algorithm.

### 网络架构

|      | 类型           |  批次  | 形状        | 备注                                                                                                      |
|:-----|:---------------|:------:|:------------|:----------------------------------------------------------------------------------------------------------|
| 输入 | image          |   1    | [32, 32, 3] | The input image should be resized to 32x32 pixels                                                         |
| 输出 | classification |   1    | [10]        | The output is a 10-dimension vector, each of which represents the probability of the corresponding class. |
### 基准测试

|  框架   |  精度   |  Top-1(%)  |  Top-5(%)  |  Flops(M)  |  Params(M)  |  Inference(ms)   |                                                                                   下载                                                                                    |     作者     |
|:-------:|:-------:|:----------:|:----------:|:----------:|:-----------:|:----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
| PyTorch | FLOAT32 |   74.76    |   98.26    |    2.10    |    1.20     |        -         |  [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/cifar10/mobilenetv2_0.35_cifar10_float32_sha1_229a650d3d6352349bbe09f27120b0ffaea03154.pth)   | Seeed Studio |
|  ONNX   | FLOAT32 |   74.76    |   98.26    |    2.10    |    1.20     |        -         |  [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/cifar10/mobilenetv2_0.35_cifar10_float32_sha1_5de550613080ddb9e9c48917abae402b72fb1f7c.onnx)  | Seeed Studio |
| TFLite  | FLOAT32 |   74.76    |   98.26    |    2.10    |    1.20     |        -         | [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/cifar10/mobilenetv2_0.35_cifar10_float32_sha1_8573efa98eb573ce709d0eeef97cac84a4a54442.tflite) | Seeed Studio |
| TFLite  |  INT8   |   74.56    |   98.29    |    2.10    |    1.20     | 13<sup>(1)</sup> |  [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/cifar10/mobilenetv2_0.35_cifar10_int8_sha1_84561285cfef22718d41b93f81853143746293d8.tflite)   | Seeed Studio |

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

