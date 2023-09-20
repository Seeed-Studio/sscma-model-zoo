# Face Detection - Swift-YOLO

[English](../en/Face_Detection_Swift-YOLO_192.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/refactor-auto-generate/notebooks/zh_CN/Face_Detection_Swift-YOLO_192.ipynb)

**版本：** 1.0.0

**类别：** Object Detection

**算法：** [Swift-YOLO](https://github.com/Seeed-Studio/SSCMA/blob/main/configs/yolov5/yolov5_tiny_1xb16_300e_coco.py)

**数据集：** [Face](https://universe.roboflow.com/detection-kgpie/face-detection-j0igc)

**类别：** `Face`

![Face Detection](https://files.seeedstudio.com/sscma/static/detection_face.png)

The model is a Swift-YOLO model trained on the Face dataset. The model can detect faces in images.

### 网络架构

|      | 类型   |  批次  | 形状          | 备注                                                                                                             |
|:-----|:-------|:------:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| 输入 | image  |   1    | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| 输出 | bbox   |   1    | [2268, 5]     | The output is a 2268x5 tensor, where 2268 is the number of candidate boxes and 5 is [x, y, w, h, score, [class]] |
### 基准测试

|  框架   |  精度   |  mAP(%)  |  MACs(MB)  |  Params(MB)  |  Peek RAM(MB)  |    Inference(ms)    |                                                                                    下载                                                                                     |     作者     |
|:-------:|:-------:|:--------:|:----------:|:------------:|:--------------:|:-------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
| PyTorch | FLOAT32 |  94.40   |   90.56    |     0.67     |       -        |          -          |      [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_sha1_f2a3f61a271c467748e26f0fd6fdd82d740512ff.pth)       | Seeed Studio |
|  ONNX   | FLOAT32 |  94.10   |     -      |     0.67     |       -        |          -          |      [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_sha1_e530c8df4b4474979cbfe2da447d06ab657289ce.onnx)      | Seeed Studio |
| TFLite  | FLOAT32 |  94.10   |    89.0    |      -       |      1.2       |          -          | [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_float32_sha1_a647ee0f7eb8951b3d78c8048159e999029d7051.tflite) | Seeed Studio |
| TFLite  |  INT8   |  93.10   |    89.0    |      -       |      0.35      | 691.0<sup>(1)</sup> |  [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/models/yolov5/Face/yolov5_tiny_1xb16_300e_coco_int8_sha1_e707d23e1b45b4a464e9ebedae0f6570a9d35a9c.tflite)   | Seeed Studio |

***表格注释：***

- ***Evaluation Parameters：***  Confidence Threshold: 0.001, IoU Threshold: 0.55, mAP Eval IoU: 0.50..*
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

