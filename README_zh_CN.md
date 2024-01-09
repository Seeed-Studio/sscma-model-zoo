# Seeed Studio SSCMA Model Zoo

<div align="center">
  <a href="https://sensecraftma.seeed.cc/" target="_blank"><img width="20%" src="https://files.seeedstudio.com/sscma/docs/images/SSCMA-Hero.png"></a>
</div>

[English](README.md) | 简体中文

## 简介

欢迎来到 Seeed Studio SSCMA Model Zoo。我们针对不同的应用场景，提供了一系列预训练的模型供您使用，配合 [Seeed Studio SSCMA](https://github.com/Seeed-Studio/ModelAssistant)，您可以对这些模型进行测试和推理，并轻松地部署到边缘计算设备上。

SSCMA Model Zoo 专注于提供在 SSCMA 优化的神经网络上训练得到的模型，这些模型针对现实应用场景，能够在嵌入式设备上实现更快和更准确的推理。

## 应用场景

目前，SSCMA Model Zoo 提供如下应用场景的预训练模型:

### Object Detection

| 模型                                                                                                 | Colab                                                                                                                                                                                                                        |
|:---------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Gender_Detection_Swift-YOLO_192](docs/zh_CN/Gender_Detection_Swift-YOLO_192.md)                   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Gender_Detection_Swift-YOLO_192.ipynb)          |
| [Digital_Meter_Water_Swift-YOLO_192](docs/zh_CN/Digital_Meter_Water_Swift-YOLO_192.md)             | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Digital_Meter_Water_Swift-YOLO_192.ipynb)       |
| [Apple_Detection_Swift-YOLO_192](docs/zh_CN/Apple_Detection_Swift-YOLO_192.md)                     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Apple_Detection_Swift-YOLO_192.ipynb)           |
| [person_Detection_Swift-YOLO_Nano_192](docs/zh_CN/person_Detection_Swift-YOLO_Nano_192.md)         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/person_Detection_Swift-YOLO_Nano_192.ipynb)     |
| [person_Detection_Swift-YOLO_192](docs/zh_CN/person_Detection_Swift-YOLO_192.md)                   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/person_Detection_Swift-YOLO_192.ipynb)          |
| [Face_Detection_Swift-YOLO_96](docs/zh_CN/Face_Detection_Swift-YOLO_96.md)                         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Face_Detection_Swift-YOLO_96.ipynb)             |
| [COCO_Detection_Swift-YOLO_320](docs/zh_CN/COCO_Detection_Swift-YOLO_320.md)                       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/COCO_Detection_Swift-YOLO_320.ipynb)            |
| [Gesture_Detection_Swift-YOLO_192](docs/zh_CN/Gesture_Detection_Swift-YOLO_192.md)                 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Gesture_Detection_Swift-YOLO_192.ipynb)         |
| [Digital_Meter_Electricity_Swift-YOLO_192](docs/zh_CN/Digital_Meter_Electricity_Swift-YOLO_192.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Digital_Meter_Electricity_Swift-YOLO_192.ipynb) |
| [Strawberry_Detection_Swift-YOLO_192](docs/zh_CN/Strawberry_Detection_Swift-YOLO_192.md)           | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Strawberry_Detection_Swift-YOLO_192.ipynb)      |

### Image Classification

| 模型                                                                                                               | Colab                                                                                                                                                                                                                               |
|:-----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MNIST_Classification_MobileNetV2_0.5_Rep_32](docs/zh_CN/MNIST_Classification_MobileNetV2_0.5_Rep_32.md)         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/MNIST_Classification_MobileNetV2_0.5_Rep_32.ipynb)     |
| [Gender_Classification_MobileNetV2_0.35_Rep_64](docs/zh_CN/Gender_Classification_MobileNetV2_0.35_Rep_64.md)     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Gender_Classification_MobileNetV2_0.35_Rep_64.ipynb)   |
| [Person_Classification_MobileNetV2_0.35_Rep_64](docs/zh_CN/Person_Classification_MobileNetV2_0.35_Rep_64.md)     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Person_Classification_MobileNetV2_0.35_Rep_64.ipynb)   |
| [Person_Classification_MobileNetV2_0.35_Rep_96](docs/zh_CN/Person_Classification_MobileNetV2_0.35_Rep_96.md)     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Person_Classification_MobileNetV2_0.35_Rep_96.ipynb)   |
| [Person_Classification_MobileNetV2_0.35_Rep_32](docs/zh_CN/Person_Classification_MobileNetV2_0.35_Rep_32.md)     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/Person_Classification_MobileNetV2_0.35_Rep_32.ipynb)   |
| [CIFAR-10_Classification_MobileNetV2_0.35_Rep_32](docs/zh_CN/CIFAR-10_Classification_MobileNetV2_0.35_Rep_32.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seeed-studio/sscma-model-zoo/blob/main/notebooks/zh_CN/CIFAR-10_Classification_MobileNetV2_0.35_Rep_32.ipynb) |



如果您需要特定场景下特定数据集的预训练模型，欢迎向我们[提交 Issues](https://github.com/Seeed-Studio/ModelAssistant-model-zoo/issues/new/choose)。

## 快速上手

如果您希望使用 SSCMA Model Zoo 提供的模型，我们建议您遵循以下步骤:

1. 根据实际需求，选择相应的应用场景并挑选合适的神经网络。您可以浏览我们给出的测试数据进行选择。
2. 下载选择好的模型。对于公开的预训练模型，您可以通过测试数据表格中的模型链接直接下载。
3. 参考 [SSCMA 文档 - 部署示例](https://sensecraftma.seeed.cc/SSCMA/zh_cn/examples/examples)在边缘计算设备上进行部署。您也可以使用 SSCMA 在您的计算机上运行我们的模型，对我们的测试结果进行复现或推理测试。

## 故障排除

如果您在使用 SSCMA Model Zoo 中预训练模型时遇到任何问题，我们建议您先按照以下步骤排查:

1. 检查下载模型的正确性。预训练模型文件名的末尾包含该模型的 SHA-1 哈希值，您可以自行计算下载模型的 SHA-1 并与模型文件名中的进行比对 (如使用 Linux 下的 `sha1sum` 命令)，校验模型一致性。
2. 搜索 [SSCMA Model Zoo - Issues](https://github.com/Seeed-Studio/ModelAssistant-model-zoo/issues) 和 [SSCMA - Issues](https://github.com/Seeed-Studio/ModelAssistant/issues)，浏览是否有其他人反馈类似的问题。

如果以上方法都不能起到帮助，或者有其他关于 SSCMA Model Zoo 的问题，请向我们[提交 Issues](https://github.com/Seeed-Studio/ModelAssistant-model-zoo/issues/new/choose)。

## 开源许可证

不同的神经网络、数据集和模型受不同的开园许可证保护，具体请参考 [LICENSES](LICENSES)。