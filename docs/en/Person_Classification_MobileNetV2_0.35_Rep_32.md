# Person Classification - MobileNetV2 0.35 Rep

English | [简体中文](../zh_CN/Person_Classification_MobileNetV2_0.35_Rep_32.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/refactor-auto-generate/notebooks/en/Person_Classification_MobileNetV2_0.35_Rep_32.ipynb)

**Version:** 1.0.0

**Category:** Image Classification

**Algorithm:** [MobileNetV2 0.35 Rep](configs/classification/mobnetv2_0.35_rep_1bx16_300e_custom.py)

**Dataset:** [VWW](https://github.com/Mxbonn/visualwakewords)

**Class:** `Not a person`, `Person`

![Person Classification](https://files.seeedstudio.com/sscma/static/person_cls.png)

The model is a vision model designed for CIFAR-10 classification. It utilizes the [SSCMA](https://github.com/Seeed-Studio/SSCMA) training and employs the MobileNetV2 (0.35) Rep algorithm.

### Network 

|        | Type           |  Batch  | Shape       | Remark                                                                                                        |
|:-------|:---------------|:-------:|:------------|:--------------------------------------------------------------------------------------------------------------|
| Input  | image          |    1    | [32, 32, 3] | The input image should be resized to 32x32 pixels                                                             |
| Output | classification |    1    | [2]         | The output is a 2-element vector, which represents the probability of the input image belonging to each class |
### Benchmark

|  Backend  |  Precision  |  Top-1(%)  |  Flops(MB)  |  Params(M)  |   Inference(ms)   |                                                                                 Download                                                                                  |    Author    |
|:---------:|:-----------:|:----------:|:-----------:|:-----------:|:-----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|  PyTorch  |   FLOAT32   |   85.22    |     34      |    2.71     |         -         |  [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/person/mobilenetv2_0.35rep_vww32_float32_sha1_c0bb3413912614cb90492eb4c2fbfbf6d3005874.pth)   | Seeed Studio |
|   ONNX    |   FLOAT32   |   80.33    |      -      |    2.71     |         -         |  [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/person/mobilenetv2_0.35rep_vww32_float32_sha1_1cf8b63ca70b701385f0fc15294593dd356ad60f.onnx)  | Seeed Studio |
|  TFLite   |   FLOAT32   |   80.34    |      -      |    2.71     |         -         | [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/person/mobilenetv2_0.35rep_vww32_float32_sha1_5231d2f72ff1668e202cf80d7735e8878f706cda.tflite) | Seeed Studio |
|  TFLite   |    INT8     |   80.23    |      -      |    0.02     | 101<sup>(1)</sup> |  [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/models/person/mobilenetv2_0.35rep_vww32_int8_sha1_a90a9f8f09ac45022ced9ded3ab84790e5b35e59.tflite)   | Seeed Studio |

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

