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