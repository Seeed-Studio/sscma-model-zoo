# Seeed Studio EdgeLab Model Zoo

<div align="center">
  <img width="100%" src="https://cdn.jsdelivr.net/gh/Seeed-Studio/EdgeLab@main/docs/public/images/EdgeLab-Logo.png">
</div>

[English](README.md) | 简体中文


## 简介

欢迎来到 Seeed Studio EdgeLab Model Zoo。我们针对不同的应用场景，提供了一系列预训练的模型供您使用，配合 [Seeed Studio EdgeLab](https://github.com/Seeed-Studio/EdgeLab)，您可以对这些模型进行测试和推理，并轻松地部署到边缘计算设备上。

EdgeLab Model Zoo 专注于提供在 EdgeLab 优化的神经网络上训练得到的模型，这些模型针对现实应用场景，能够在嵌入式设备上实现更快和更准确的推理。


## 应用场景

目前，EdgeLab Model Zoo 提供如下应用场景的预训练模型:

- [分类](classification/README_zh-CN.md)
- [检测](detection/README_zh-CN.md)
- [姿态](pose/README_zh-CN.md)

如果您需要特定场景下特定数据集的预训练模型，欢迎向我们[提交 Issues](https://github.com/Seeed-Studio/edgelab-model-zoo/issues/new)。


## 快速上手

如果您希望使用 EdgeLab Model Zoo 提供的模型，我们建议您遵循以下步骤:

1. 根据实际需求，选择相应的应用场景并挑选合适的神经网络。您可以浏览我们给出的测试数据进行选择。
2. 下载选择好的模型。对于公开的预训练模型，您可以通过测试数据表格中的模型链接直接下载。
3. 参考 [EdgeLab 文档 - 部署示例](https://seeed-studio.github.io/EdgeLab/zh_cn/examples/examples)在边缘计算设备上进行部署。您也可以使用 EdgeLab 在您的计算机上运行我们的模型，对我们的测试结果进行复现或推理测试。


## 故障排除

如果您在使用 EdgeLab Model Zoo 中预训练模型时遇到任何问题，我们建议您先按照以下步骤排查:

1. 检查下载模型的正确性。预训练模型文件名的末尾包含该模型的 SHA-1 哈希值，您可以自行计算下载模型的 SHA-1 并与模型文件名中的进行比对 (如使用 Linux 下的 `sha1sum` 命令)，校验模型一致性。
2. 搜索 [EdgeLab Model Zoo - Issues](https://github.com/Seeed-Studio/edgelab-model-zoo/issues) 和 [EdgeLab - Issues](https://github.com/Seeed-Studio/EdgeLab/issues)，浏览是否有其他人反馈类似的问题。

如果以上方法都不能起到帮助，或者有其他关于 EdgeLab Model Zoo 的问题，请向我们[提交 Issues](https://github.com/Seeed-Studio/edgelab-model-zoo/issues/new)。


## 开源许可证

不同的神经网络、数据集和模型受不同的开园许可证保护，具体请参考 [LICENSES](LICENSES)。
