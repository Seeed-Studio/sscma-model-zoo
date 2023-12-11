# Person Classification - MobileNetV2 0.35 Rep

English | [简体中文](../zh_CN/Person_Classification_MobileNetV2_0.35_Rep_96.md) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/en/Person_Classification_MobileNetV2_0.35_Rep_96.ipynb)

**Version:** 1.0.0

**Category:** Image Classification

**Algorithm:** [MobileNetV2 0.35 Rep](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/classification/mobnetv2_0.35_rep_1bx16_300e_custom.py)

**Dataset:** [VWW](https://github.com/Mxbonn/visualwakewords)

**Class:** `Not a person`, `Person`

![Person Classification](https://files.seeedstudio.com/sscma/static/person_cls.png)

The model is a vision model designed for CIFAR-10 classification. It utilizes the [SSCMA](https://github.com/Seeed-Studio/SSCMA) training and employs the MobileNetV2 (0.35) Rep algorithm.

### Network 

|        | Type           |  Batch  | Shape       | Remark                                                                                                        |
|:-------|:---------------|:-------:|:------------|:--------------------------------------------------------------------------------------------------------------|
| Input  | image          |    1    | [96, 96, 3] | The input image should be resized to 96x96 pixels                                                             |
| Output | classification |    1    | [2]         | The output is a 2-element vector, which represents the probability of the input image belonging to each class |
### Benchmark

|   Backend    |  Precision  |  Top-1(%)  |  Flops(MB)  |  Params(M)  |   Inference(ms)    |                                                                               Download                                                                               |    Author    |
|:------------:|:-----------:|:----------:|:-----------:|:-----------:|:------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    |   FLOAT32   |   88.37    |    76.5     |    2.71     |         -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww96_float32_sha1_0b47deccb4ffab4d8f970ea6379b838163e5bd8f.pth)    | Seeed Studio |
|     ONNX     |   FLOAT32   |   88.36    |      -      |    2.71     |         -          |   [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww96_float32_sha1_689cbad95dc725880861e72b5b9f7878f04ce17f.onnx)   | Seeed Studio |
|    TFLite    |   FLOAT32   |   88.36    |      -      |    2.71     |         -          |  [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww96_float32_sha1_a92eb1b9420f2947bfb65153e1def12097fdb977.tflite)  | Seeed Studio |
|    TFLite    |    INT8     |   88.27    |      -      |    2.71     | 582<sup>(1)</sup>  |   [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww96_int8_sha1_f1a66ce5a3f05bc1293920e5a95f547e27df6550.tflite)    | Seeed Studio |
| TFLite(vela) |    INT8     |   88.27    |      -      |    2.71     | 15.0<sup>(2)</sup> | [Link](https://files.seeedstudio.com/sscma/model_zoo/classification/person/mobilenetv2_0.35rep_vww96_int8_sha1_f1a66ce5a3f05bc1293920e5a95f547e27df6550_vela.tflite) | Seeed Studio |

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

