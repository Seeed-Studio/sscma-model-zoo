# MNIST Classification - MobileNetV2(0.5) Rep

[English](../en/MNIST_Classification_MobileNetV2(0.5)_Rep_32.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/refactor-auto-generate/notebooks/zh_CN/MNIST_Classification_MobileNetV2(0.5)_Rep_32.ipynb)

**版本：** 1.0.0

**类别：** Image Classification

**算法：** [MobileNetV2(0.5) Rep](https://raw.githubusercontent.com/Seeed-Studio/SSCMA/main/configs/classification/mobnetv2_0.35_rep_1bx16_300e_cifar10.py)

**数据集：** [MNIST](http://yann.lecun.com/exdb/mnist/)

**类别：** `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`

![MNIST Classification](https://files.seeedstudio.com/sscma/static/mnist_cls.png)

The model is a vision model designed for MNIST dataset

### 网络架构

|      | 类型           |  批次  | 形状        | 备注                                                                                                      |
|:-----|:---------------|:------:|:------------|:----------------------------------------------------------------------------------------------------------|
| 输入 | image          |   1    | [32, 32, 1] | The input image should be resized to 32x32 pixels                                                         |
| 输出 | classification |   1    | [10]        | The output is a 10-dimension vector, each of which represents the probability of the corresponding class. |
### 基准测试

|  框架   |  精度   |  Top-1(%)  |  Top-5(%)  |  Flops(MB)  |  Params(MB)  |  Inference(ms)   |                                                                                  下载                                                                                  |     作者     |
|:-------:|:-------:|:----------:|:----------:|:-----------:|:------------:|:----------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
| PyTorch | FLOAT32 |   99.01    |    1.00    |    0.21     |     0.08     |        -         |   [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_float32_sha1_41b743d3bceb50b5b677c7688567a87612e8435a.pth)   | Seeed Studio |
|  ONNX   | FLOAT32 |   99.01    |    1.00    |      -      |     0.08     |        -         |  [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_float32_sha1_068ee0fe613d40158cecd34427bbf52b1bc2d738.onnx)   | Seeed Studio |
| TFLite  | FLOAT32 |   99.01    |    1.00    |      -      |     0.72     |        -         | [链接]( https://files.seeedstudio.com/sscma/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_float32_sha1_b27cb353f199e0378783585790c2798186f6a000.tflite) | Seeed Studio |
| TFLite  |  INT8   |   98.98    |   99.98    |      -      |     0.02     | 13<sup>(1)</sup> |   [链接](https://files.seeedstudio.com/sscma/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_int8_sha1_ae68f9558b3808650005587411d04a87a441300c.tflite)   | Seeed Studio |

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

