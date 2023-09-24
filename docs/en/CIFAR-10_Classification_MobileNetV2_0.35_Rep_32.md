# CIFAR-10 Classification - MobileNetV2 0.35 Rep

English | [简体中文](../zh_CN/CIFAR-10_Classification_MobileNetV2_0.35_Rep_32.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/CIFAR-10_Classification_MobileNetV2_0.35_Rep_32.ipynb)

**Version:** 1.0.0

**Category:** Image Classification

**Algorithm:** [MobileNetV2 0.35 Rep](configs/classification/mobnetv2_0.35_rep_1bx16_300e_cifar10.py)

**Dataset:** [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html)

**Class:** `Airplane`, `Automobile`, `Bird`, `Cat`, `Deer`, `Dog`, `Frog`, `Horse`, `Ship`, `Truck`

![CIFAR-10 Classification](https://files.seeedstudio.com/sscma/static/cifar10_cls_0_35.png)

The model is a vision model designed for CIFAR-10 classification. It utilizes the [SSCMA](https://github.com/Seeed-Studio/SSCMA) training and employs the MobileNetV2 (0.35) Rep algorithm.

### Network 

|        | Type           |  Batch  | Shape       | Remark                                                                                                    |
|:-------|:---------------|:-------:|:------------|:----------------------------------------------------------------------------------------------------------|
| Input  | image          |    1    | [32, 32, 3] | The input image should be resized to 32x32 pixels                                                         |
| Output | classification |    1    | [10]        | The output is a 10-dimension vector, each of which represents the probability of the corresponding class. |
### Benchmark

|  Backend  |  Precision  |  Top-1(%)  |  Top-5(%)  |  Flops(M)  |  Params(M)  |  Inference(ms)   |                                                                                 Download                                                                                  |    Author    |
|:---------:|:-----------:|:----------:|:----------:|:----------:|:-----------:|:----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|  PyTorch  |   FLOAT32   |   74.76    |   98.26    |    2.10    |    1.20     |        -         |  [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/cifar10/mobilenetv2_0.35_cifar10_float32_sha1_229a650d3d6352349bbe09f27120b0ffaea03154.pth)   | Seeed Studio |
|   ONNX    |   FLOAT32   |   74.76    |   98.26    |    2.10    |    1.20     |        -         |  [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/cifar10/mobilenetv2_0.35_cifar10_float32_sha1_5de550613080ddb9e9c48917abae402b72fb1f7c.onnx)  | Seeed Studio |
|  TFLite   |   FLOAT32   |   74.76    |   98.26    |    2.10    |    1.20     |        -         | [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/cifar10/mobilenetv2_0.35_cifar10_float32_sha1_8573efa98eb573ce709d0eeef97cac84a4a54442.tflite) | Seeed Studio |
|  TFLite   |    INT8     |   74.56    |   98.29    |    2.10    |    1.20     | 13<sup>(1)</sup> |  [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/cifar10/mobilenetv2_0.35_cifar10_int8_sha1_84561285cfef22718d41b93f81853143746293d8.tflite)   | Seeed Studio |

***Table Notes:***

- ***Backend:** The deep learning framework used to infer the model.*
- ***Precision:** The numerical precision used for training the model.*
- ***Metrics:** The metrics used to evaluate the model.*
- ***Inference(ms):** The inference time of the model in milliseconds.*
  - ***1:** xiao_esp32s3.*
- ***Link:** The link to the model.*
- ***Author:** The author of the model.*

### License

MIT

