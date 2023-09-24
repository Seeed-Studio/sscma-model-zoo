# MNIST Classification - MobileNetV2 0.5 Rep

English | [简体中文](../zh_CN/MNIST_Classification_MobileNetV2_0.5_Rep_32.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/refactor-auto-generate/notebooks/en/MNIST_Classification_MobileNetV2_0.5_Rep_32.ipynb)

**Version:** 1.0.0

**Category:** Image Classification

**Algorithm:** [MobileNetV2 0.5 Rep](configs/classification/mobnetv2_0.35_rep_1bx16_300e_mnist.py)

**Dataset:** [MNIST](http://yann.lecun.com/exdb/mnist/)

**Class:** `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`

![MNIST Classification](https://files.seeedstudio.com/sscma/static/mnist_cls.png)

The model is a vision model designed for MNIST dataset

### Network 

|        | Type           |  Batch  | Shape       | Remark                                                                                                    |
|:-------|:---------------|:-------:|:------------|:----------------------------------------------------------------------------------------------------------|
| Input  | image          |    1    | [32, 32, 1] | The input image should be resized to 32x32 pixels                                                         |
| Output | classification |    1    | [10]        | The output is a 10-dimension vector, each of which represents the probability of the corresponding class. |
### Benchmark

|  Backend  |  Precision  |  Top-1(%)  |  Top-5(%)  |  Flops(MB)  |  Params(M)  |  Inference(ms)   |                                                                                Download                                                                                |    Author    |
|:---------:|:-----------:|:----------:|:----------:|:-----------:|:-----------:|:----------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|  PyTorch  |   FLOAT32   |   99.01    |    1.00    |     2.1     |    1.20     |        -         |   [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_float32_sha1_41b743d3bceb50b5b677c7688567a87612e8435a.pth)   | Seeed Studio |
|   ONNX    |   FLOAT32   |   99.01    |    1.00    |      -      |    1.20     |        -         |  [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_float32_sha1_068ee0fe613d40158cecd34427bbf52b1bc2d738.onnx)   | Seeed Studio |
|  TFLite   |   FLOAT32   |   99.01    |    1.00    |      -      |    1.20     |        -         | [Link]( https://files.seeedstudio.com/sscma/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_float32_sha1_b27cb353f199e0378783585790c2798186f6a000.tflite) | Seeed Studio |
|  TFLite   |    INT8     |   98.98    |   99.98    |      -      |    1.20     | 13<sup>(1)</sup> |   [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_int8_sha1_ae68f9558b3808650005587411d04a87a441300c.tflite)   | Seeed Studio |

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

