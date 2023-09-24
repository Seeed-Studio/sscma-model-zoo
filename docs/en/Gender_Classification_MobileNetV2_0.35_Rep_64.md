# Gender Classification - MobileNetV2 0.35 Rep

English | [简体中文](../zh_CN/Gender_Classification_MobileNetV2_0.35_Rep_64.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/refactor-auto-generate/notebooks/en/Gender_Classification_MobileNetV2_0.35_Rep_64.ipynb)

**Version:** 1.0.0

**Category:** Image Classification

**Algorithm:** [MobileNetV2 0.35 Rep](configs/classification/mobnetv2_0.35_rep_1bx16_300e_custom.py)

**Dataset:** [Gender](https://universe.roboflow.com/seeed-studio-e2fso/gender-8vbxd)

**Class:** `Not a person`, `Person`

![Gender Classification](https://files.seeedstudio.com/sscma/static/gender_cls.png)

The model is a vision model designed for Gender classification. It utilizes the [SSCMA](https://github.com/Seeed-Studio/SSCMA) training and employs the MobileNetV2 (0.35) Rep algorithm.

### Network 

|        | Type           |  Batch  | Shape       | Remark                                                                                                        |
|:-------|:---------------|:-------:|:------------|:--------------------------------------------------------------------------------------------------------------|
| Input  | image          |    1    | [64, 64, 3] | The input image should be resized to 64x64 pixels                                                             |
| Output | classification |    1    | [2]         | The output is a 2-element vector, which represents the probability of the input image belonging to each class |
### Benchmark

|  Backend  |  Precision  |  Top-1(%)  |  Flops(M)  |  Params(M)  |  Inference(ms)   |                                                                          Download                                                                          |    Author    |
|:---------:|:-----------:|:----------:|:----------:|:-----------:|:----------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|  PyTorch  |   FLOAT32   |   94.50    |    5.49    |    2.16     |        -         | [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/gender/mbv2_0.35_rep_gender_sha1_62336a001f0cd58d2ac8ed5a6823b9ac7374f276.pth)  | Seeed Studio |
|   ONNX    |   FLOAT32   |   94.50    |     -      |    2.16     |        -         |   [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/gender/mbv2_0.35_rep_gender_a9031151303fb4eaeae99262d26c0719a7bca7d7.onnx)    | Seeed Studio |
|  TFLite   |   FLOAT32   |   94.50    |     -      |    2.16     |        -         |  [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/gender/mbv2_0.35_rep_gender_5e6dc80bd5f3ddb429326a27f767816d998c919b.tflite)   | Seeed Studio |
|  TFLite   |    INT8     |   94.30    |     -      |    2.16     | 40<sup>(1)</sup> | [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/gender/mbv2_0.35_rep_gender_int8_sha1_2bc5677615f8aeb41bffe21e25de6d01f91c3a41.tflite) | Seeed Studio |

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

