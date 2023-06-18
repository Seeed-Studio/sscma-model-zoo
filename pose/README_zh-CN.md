## 模型概述

pose模型库包含了使用不同优化的神经网络在[EdgeLab](https://github.com/Seeed-Studio/EdgeLab)中训练的预训练模型。

检测目录的层次结构如下所示：

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


`models`文件夹包含了不同的神经网络，每个神经网络用其名称表示，位于`<网络名称>`文件夹中。在神经网络文件夹内，模型可能在不同的数据集上进行训练，因此我们使用`<数据集名称>`将这些预训练模型划分到不同的文件夹中。


## 模型性能

本部分总结了来自不同神经网络训练的不同模型的性能。

### PFLD MoblieNetV2

| 模型名称 | 后端 | 数据集 | 输入尺寸 | ACC | MACs (M) | 参数数量 (M) | 调用内存 (MiB) | 调用时间 (ms) | 链接 |
|--|--|--|--|--|--|--|--|--|--|
| pfld_mobilenetv2 | PyTorch | WFLW | 112x112x3 | TODO | TODO | TODO | TODO | TODO| [下载Github](TODO)|


## 模型示例

本部分显示了从不同数据集训练的模型示例。

### PFLD MobileNetv2

| 模型名称 | 后端 | 数据集 | 输入尺寸 | ACC | 调用时间 (ms) | 链接 |
|--|--|--|--|--|--|--|
| pfld_mobilenetv2 | TFLite | [pointer meter](TODO) | 112x112x3 | TODO | TODO | [下载Github](TODO)|