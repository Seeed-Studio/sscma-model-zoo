# Classification 概述

图像分类 Model Zoo 包含多个使用不同神经网络的预训练模型，这些模型是在 [EdgeLab](https://github.com/Seeed-Studio/EdgeLab) 优化的神经网络上训练的。

检测目录的层次结构如下：

```txt
detection
├── models
│   ├── <network name>
│   │   ├── <datasets name>
│   │   │   ├── <pre-trained model>
│   │   │   └── ...
│   │   └── ...
│   └── ...
└── ...
```

文件夹 `models` 包含不同神经网络的预训练模型，各模型以其神经网络的名称表示，位于 `<network name>` 文件夹内。在对应模型的神经网络文件夹内，模型可能在不同的数据集上进行训练，因此我们使用 `<datasets name>` 来将这些预训练模型以实际训练的数据集划分到不同的文件夹中。


## 模型性能

本节总结了由不同神经网络训练的不同模型的性能。


## Performance of Models

The section summarizes the performance of different models trained from different neural networks.

### MobileNetV2(0.35) Rep

| Model Name | Backend | Datasets | Input Size | Precision |Top-1(%) | Top-5(%) | Flops (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|--|--|
|MobileNetV2(0.35) Rep| PyTorch | CIFAR10 | 32x32x3 | Float32 | 62.1 | 96.3| 0.21 | 0.021 | - | 22<sup>(2)(3) | [Download]() |


### MobileNetV2(1.0) 

| Model Name | Backend | Datasets | Input Size | Precision |Top-1(%) | Top-5(%) | Flops (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|--|--|
|MobileNetV2(1.0)| PyTorch | CIFAR10 | 32x32x3 | Float32 | 84.0 | 99.0| 6.4 | 2.237 | - | - | [Download]() |

*注:*

<sup>1</sup> Measured on [ESP32-S3 (XIAO)](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/).

<sup>2</sup> Measured on [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/).

<sup>3</sup> Measured on [SenseCAP A1101](https://wiki.seeedstudio.com/SenseCAP-Vision-AI-Get-Started/).


