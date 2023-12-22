# Person Classification - MobileNetV2 0.35 Rep

English | [简体中文](../zh_CN/Person_Classification_MobileNetV2_0.35_Rep_64.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/Person_Classification_MobileNetV2_0.35_Rep_64.ipynb)

**Version:** 1.0.0

**Category:** Image Classification

**Algorithm:** [MobileNetV2 0.35 Rep](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/classification/mobnetv2_0.35_rep_1bx16_300e_custom.py)

**Dataset:** [VWW](https://github.com/Mxbonn/visualwakewords)

**Class:** `Not a person`, `Person`

![Person Classification](https://files.seeedstudio.com/sscma/static/person_cls.png)

The model is a vision model designed for person classification. It utilizes the [SSCMA](https://github.com/Seeed-Studio/ModelAssistant) training and employs the MobileNetV2 (0.35) Rep algorithm.

### Network 

|        | Type           |  Batch  | Shape       | Remark                                                                                                        |
|:-------|:---------------|:-------:|:------------|:--------------------------------------------------------------------------------------------------------------|
| Input  | image          |    1    | [64, 64, 3] | The input image should be resized to 64x64 pixels                                                             |
| Output | classification |    1    | [2]         | The output is a 2-element vector, which represents the probability of the input image belonging to each class |
### Benchmark

|   Backend    |  Precision  |  Top-1(%)  |  Flops(MB)  |  Params(M)  |   Inference(ms)   |                                                                               Download                                                                               |    Author    |
|:------------:|:-----------:|:----------:|:-----------:|:-----------:|:-----------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    |   FLOAT32   |   85.22    |     34      |    2.71     |         -         |   [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww64_float32_sha1_6dec3c029041408de043c5921621ab7abc4c4ec4.pth)    | Seeed Studio |
|     ONNX     |   FLOAT32   |   85.23    |      -      |    2.71     |         -         |   [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww64_float32_sha1_aeb9c1f3bf7c19f3490daee7da1ac0d76b7e49d9.onnx)   | Seeed Studio |
|    TFLite    |   FLOAT32   |   85.23    |      -      |    2.71     |         -         |  [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww64_float32_sha1_d44e8c1247dfc66e645f5d07b904e4a430149882.tflite)  | Seeed Studio |
|    TFLite    |    INT8     |   85.26    |      -      |    2.71     | 286<sup>(1)</sup> |   [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww64_int8_sha1_a939407d507b45ceca293e74c8961d59357b37b2.tflite)    | Seeed Studio |
| TFLite(vela) |    INT8     |   85.26    |      -      |    2.71     | 8.0<sup>(2)</sup> | [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww64_int8_sha1_a939407d507b45ceca293e74c8961d59357b37b2_vela.tflite) | Seeed Studio |

***Table Notes:***

- ***Backend:** The deep learning framework used to infer the model.*
- ***Precision:** The numerical precision used for training the model.*
- ***Metrics:** The metrics used to evaluate the model.*
- ***Inference(ms):** The inference time of the model in milliseconds.*
  - ***1:** xiao_esp32s3.*
  - ***2:** grove_vision_ai_we2.*
- ***Link:** The link to the model.*
- ***Author:** The author of the model.*

### License

MIT

