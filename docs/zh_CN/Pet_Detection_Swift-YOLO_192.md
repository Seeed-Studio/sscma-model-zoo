# Pet Detection - Swift-YOLO

[English](../en/Pet_Detection_Swift-YOLO_192.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Pet_Detection_Swift-YOLO_192.ipynb)

**版本：** 1.0.0

**任务** Object Detection

**算法：** [Swift-YOLO](https://github.com/Seeed-Studio/ModelAssistant/blob/main/configs/swift_yolo/swift_yolo_tiny_1xb16_300e_coco.py)

**数据集：** [Animal](https://universe.roboflow.com/animal-cegrr/animal-ph37i/dataset/11)

**类别** `cat`, `dog`

![Pet Detection](https://files.seeedstudio.com/sscma/static/detection_animal.png)

The model is a Swift-YOLO model trained on the animal detection dataset for cat and dog.

### 网络架构

|    | 类型    |  批次  | 形状            | 备注                                                                                                               |
|:---|:------|:----:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| 输入 | image |  1   | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| 输出 | bbox  |  1   | [2268, 7]     | The output is a 2268x7 tensor, where 2268 is the number of candidate boxes and 7 is [x, y, w, h, score, [class]] |
### 基准测试

|      框架      |   精度    |  mAP(%)  |  Flops(M)  |  Params(M)  |    Inference(ms)    |                                                   下载                                                   |      作者      |
|:------------:|:-------:|:--------:|:----------:|:-----------:|:-------------------:|:------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    | FLOAT32 |  93.30   |   90.685   |     0.7     |          -          |       [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/animal/animal_detection.pth)        | Seeed Studio |
|     ONNX     | FLOAT32 |  88.30   |     -      |     0.7     |          -          |   [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/animal/animal_detection_float32.onnx)   | Seeed Studio |
|    TFLite    | FLOAT32 |  88.30   |     -      |      -      |          -          |  [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/animal/animal_detection_float32.tflite)  | Seeed Studio |
|    TFLite    |  INT8   |  87.10   |     -      |      -      | 706.0<sup>(1)</sup> |   [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/animal/animal_detection_int8.tflite)    | Seeed Studio |
| TFLite(vela) |  INT8   |  87.10   |     -      |      -      |  45<sup>(2)</sup>   | [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/animal/animal_detection_int8_vela.tflite) | Seeed Studio |

***表格注释：***

- ***Evaluation Parameters：***  Confidence Threshold: 0.001, IoU Threshold: 0.55, mAP Eval IoU: 0.50..*
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

