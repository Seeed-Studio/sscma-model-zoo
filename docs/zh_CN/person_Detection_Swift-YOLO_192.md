# person Detection - Swift-YOLO

[English](../en/person_Detection_Swift-YOLO_192.md) | 简体中文 [![在Colab中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/person_Detection_Swift-YOLO_192.ipynb)

**版本：** 1.0.0

**任务** Object Detection

**算法：** [Swift-YOLO](configs/yolov5/swift_yolo_shuff_1xb16_300e_coco.py)

**数据集：** [](https://app.roboflow.com/hanzhou-7mktt/ssperson/7)

**类别** `person`, `bicycle`, `car`, `motorcycle`, `airplane`, `bus`, `train`, `truck`, `boat`, `traffic light`, `fire hydrant`, `stop sign`, `parking meter`, `bench`, `bird`, `cat`, `dog`, `horse`, `sheep`, `cow`, `elephant`, `bear`, `zebra`, `giraffe`, `backpack`, `umbrella`, `handbag`, `tie`, `suitcase`, `frisbee`, `skis`, `snowboard`, `sports ball`, `kite`, `baseball bat`, `baseball glove`, `skateboard`, `surfboard`, `tennis racket`, `bottle`, `wine glass`, `cup`, `fork`, `knife`, `spoon`, `bowl`, `banana`, `apple`, `sandwich`, `orange`, `broccoli`, `carrot`, `hot dog`, `pizza`, `donut`, `cake`, `chair`, `couch`, `potted plant`, `bed`, `dining table`, `toilet`, `tv`, `laptop`, `mouse`, `remote`, `keyboard`, `cell phone`, `microwave`, `oven`, `toaster`, `sink`, `refrigerator`, `book`, `clock`, `vase`, `scissors`, `teddy bear`, `hair drier`, `toothbrush`

![person Detection](https://files.seeedstudio.com/sscma/static/detection_coco.png)

The model is a Swift-YOLO model trained on the person detection dataset.

### 网络架构

|    | 类型    |  批次  | 形状            | 备注                                                                                                               |
|:---|:------|:----:|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| 输入 | image |  1   | [192, 192, 3] | The input image should be resized to 192x192 pixels.                                                             |
| 输出 | bbox  |  1   | [2268, 6]     | The output is a 2268x6 tensor, where 2268 is the number of candidate boxes and 6 is [x, y, w, h, score, [class]] |
### 基准测试

|      框架      |   精度    |  mAP(%)  |  Flops(M)  |  Params(M)  |  Peek RAM(MB)  |    Inference(ms)    |                                                                               下载                                                                                |      作者      |
|:------------:|:-------:|:--------:|:----------:|:-----------:|:--------------:|:-------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|
|   PyTorch    | FLOAT32 |  95.40   |    194     |     0.7     |       -        |          -          |   [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/person/swift_yolo_shuffle_coco_320_float32_sha1_a5927bd6a6c6569d27edb98da946a8e75a8d816f.pth)    | Seeed Studio |
|     ONNX     | FLOAT32 |  95.40   |     -      |     0.7     |       -        |          -          |   [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/person/swift_yolo_shuffle_coco_320_float32_sha1_20bc2c8517a8e42699bf46f1409f7541e52345ac.onnx)   | Seeed Studio |
|    TFLite    | FLOAT32 |  95.40   |     -      |      -      |      1.2       |          -          |  [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/person/swift_yolo_shuffle_coco_320_float32_sha1_5dfa1a16d27ef347c0173c5297395963760fcc57.tflite)  | Seeed Studio |
|    TFLite    |  INT8   |  91.70   |     -      |      -      |      0.35      | 200.0<sup>(1)</sup> |   [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/person/swift_yolo_shuffle_coco_320_int8_sha1_3b0a6d7fd95e9dd21902beae6fa2d1cd0807bd7b.tflite)    | Seeed Studio |
| TFLite(vela) |  INT8   |  91.70   |     -      |      -      |      0.35      | 46.0<sup>(2)</sup>  | [链接](https://files.seeedstudio.com/sscma/model_zoo/detection/person/swift_yolo_shuffle_coco_320_int8_sha1_3b0a6d7fd95e9dd21902beae6fa2d1cd0807bd7b_vela.tflite) | Seeed Studio |

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

