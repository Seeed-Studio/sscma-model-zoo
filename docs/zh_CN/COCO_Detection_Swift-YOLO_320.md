# COCO Detection - Swift-YOLO

[English](../en/COCO_Detection_Swift-YOLO_320.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/COCO_Detection_Swift-YOLO_320.ipynb)

**版本：** 1.0.0

**任务** Object Detection

**算法：** [Swift-YOLO](configs/yolov5/swift_yolo_shuff_1xb16_300e_coco.py)

**数据集：** [COCO2017](https://public.roboflow.com/object-detection/microsoft-coco-subset)

**类别** `person`

![COCO Detection](https://files.seeedstudio.com/sscma/static/detection_coco.png)

The model is a Swift-YOLO model trained on the COCO2017 dataset.

### 网络架构

|      | 类型   |  批次  | 形状          | 备注                                                                                                              |
|:-----|:-------|:------:|:--------------|:------------------------------------------------------------------------------------------------------------------|
| 输入 | image  |   1    | [320, 320, 3] | The input image should be resized to 320x320 pixels.                                                              |
| 输出 | bbox   |   1    | [6300, 85]    | The output is a 6300x85 tensor, where 6300 is the number of candidate boxes and 5 is [x, y, w, h, score, [class]] |
### 基准测试

|     框架     |  精度   |  mAP(%)  |  Flops(M)  |  Params(M)  |  Peek RAM(MB)  |    Inference(ms)    |                                                                              下载                                                                               |     作者     |
|:------------:|:-------:|:--------:|:----------:|:-----------:|:--------------:|:-------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    | FLOAT32 |  25.10   |    194     |    0.63     |       -        |          -          |   [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/coco/swift_yolo_shuffle_coco_320_float32_sha1_a5927bd6a6c6569d27edb98da946a8e75a8d816f.pth)    | Seeed Studio |
|     ONNX     | FLOAT32 |  25.10   |     -      |    0.63     |       -        |          -          |   [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/coco/swift_yolo_shuffle_coco_320_float32_sha1_20bc2c8517a8e42699bf46f1409f7541e52345ac.onnx)   | Seeed Studio |
|    TFLite    | FLOAT32 |  25.10   |     -      |      -      |      1.2       |          -          |  [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/coco/swift_yolo_shuffle_coco_320_float32_sha1_5dfa1a16d27ef347c0173c5297395963760fcc57.tflite)  | Seeed Studio |
|    TFLite    |  INT8   |  25.10   |     -      |      -      |      0.35      | 200.0<sup>(1)</sup> |   [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/coco/swift_yolo_shuffle_coco_320_int8_sha1_3b0a6d7fd95e9dd21902beae6fa2d1cd0807bd7b.tflite)    | Seeed Studio |
| TFLite(vela) |  INT8   |  25.10   |     -      |      -      |      0.35      | 20.0<sup>(2)</sup>  | [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/coco/swift_yolo_shuffle_coco_320_int8_sha1_3b0a6d7fd95e9dd21902beae6fa2d1cd0807bd7b_vela.tflite) | Seeed Studio |

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

