# Classification 概述

图像分类 Model Zoo 包含多个使用不同神经网络的预训练模型，这些模型是在 [SSCMA](https://github.com/Seeed-Studio/SSCMA) 优化的(更轻量化，速度更快)神经网络上训练的。


分类目录的层次结构如下：

```txt
classification
├── <任务>
│   ├── <模型>
│   └── ...
└── ...
```

## 任务场景

模型按照目标任务进行分类，可方便用户寻找适合自己任务需求的模型方案。

- [CIFAR](./cifar/README.md)
- [MNIST](./mnist/README.md)
- [EMOTION](./emotion/README.md)
- [PERSON](./person/README.md)

## 模型性能

本节总结了由不同神经网络训练的不同模型的性能。

## Performance of Models

The section summarizes the performance of different models trained from different neural networks.

### MobileNetV2(0.35) Rep

| Model Name | Backend | Datasets | Input Size | Precision |Top-1(%) | Top-5(%) | Flops (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms) | Link |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|MobileNetV2(0.35) Rep| PyTorch | CIFAR10 | 32x32x3 | Float32 | 74.76 | 98.26| 0.21 | 0.021 | - | 22<sup>(2)(3) | [Download](https://files.seeedstudio.com/edgelab/model_zoo/classification/models/cifar10/mobilenetv2_cifar10_float32_sha1_229a650d3d6352349bbe09f27120b0ffaea03154.pth) |
|MobileNetV2(0.35) Rep| onnx | CIFAR10 | 32x32x3 | Float32 | 74.76 | 98.26| 0.21 | 0.021 | - | 22<sup>(2)(3) | [Download](https://files.seeedstudio.com/edgelab/model_zoo/classification/models/cifar10/mobilenetv2_cifar10_float32_sha1_5de550613080ddb9e9c48917abae402b72fb1f7c.onnx) |
|MobileNetV2(0.35) Rep| tflite | CIFAR10 | 32x32x3 | Float32 | 74.76 | 98.26| 0.21 | 0.021 | - | 22<sup>(2)(3) | [Download](https://files.seeedstudio.com/edgelab/model_zoo/classification/models/cifar10/mobilenetv2_cifar10_float32_sha1_8573efa98eb573ce709d0eeef97cac84a4a54442.tflite) |
|MobileNetV2(0.35) Rep| tflite | CIFAR10 | 32x32x3 | int8(PTQ) | 74.56 | 98.29| 0.21 | 0.021 | - | 22<sup>(2)(3) | [Download](https://files.seeedstudio.com/edgelab/model_zoo/classification/models/cifar10/mobilenetv2_cifar10_int8_sha1_84561285cfef22718d41b93f81853143746293d8.tflite) |
|MobileNetV2(0.35) Rep| PyTorch | MNIST | 32x32x1 | Float32 | 99.01 | 1 | 0.21 | 0.021 | - | 22<sup>(2)(3) | [Download](https://files.seeedstudio.com/edgelab/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_float32_sha1_41b743d3bceb50b5b677c7688567a87612e8435a.pth) |
|MobileNetV2(0.35) Rep| onnx | MNIST | 32x32x1 | Float32 | 99.01 | 1 | 0.21 | 0.021 | - | 22<sup>(2)(3) | [Download](https://files.seeedstudio.com/edgelab/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_float32_sha1_068ee0fe613d40158cecd34427bbf52b1bc2d738.onnx) |
|MobileNetV2(0.35) Rep| tflite | MNIST | 32x32x1 | Float32 | 99.01 | 1 | 0.21 | 0.021 | - | 22<sup>(2)(3) | [Download](https://files.seeedstudio.com/edgelab/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_float32_sha1_b27cb353f199e0378783585790c2798186f6a000.tflite) |
|MobileNetV2(0.35) Rep| tflite | MNIST | 32x32x1 | int8(PTQ) | 98.98 | 99.98| 0.21 | 0.021 | - | 22<sup>(2)(3) | [Download](https://files.seeedstudio.com/edgelab/model_zoo/classification/models/mnist/mobilenetv2_0.35_mnist_int8_sha1_ae68f9558b3808650005587411d04a87a441300c.tflite) |

### MobileNetV2(1.0)

| Model Name | Backend | Datasets | Input Size | Precision |Top-1(%) | Top-5(%) | Flops (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms) | Link |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|MobileNetV2(1.0)| PyTorch | CIFAR10 | 32x32x3 | Float32 | 84.0 | 99.0| 6.4 | 2.237 | - | - | [Download]() |

*注:*

<sup>1</sup> Measured on [ESP32-S3 (XIAO)](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/).

<sup>2</sup> Measured on [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/).

<sup>3</sup> Measured on [SenseCAP A1101](https://wiki.seeedstudio.com/SenseCAP-Vision-AI-Get-Started/).

