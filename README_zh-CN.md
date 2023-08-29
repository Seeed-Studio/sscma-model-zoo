# Seeed Studio SSCMA Model Zoo

<div align="center">
  <img width="100%" src="https://cdn.jsdelivr.net/gh/Seeed-Studio/SSCMA@main/docs/public/images/SSCMA-Logo.png">
</div>

[English](README.md) | 简体中文

## 简介

欢迎来到 Seeed Studio SSCMA Model Zoo。我们针对不同的应用场景，提供了一系列预训练的模型供您使用，配合 [Seeed Studio SSCMA](https://github.com/Seeed-Studio/SSCMA)，您可以对这些模型进行测试和推理，并轻松地部署到边缘计算设备上。

SSCMA Model Zoo 专注于提供在 SSCMA 优化的神经网络上训练得到的模型，这些模型针对现实应用场景，能够在嵌入式设备上实现更快和更准确的推理。

## 应用场景

目前，SSCMA Model Zoo 提供如下应用场景的预训练模型:

- [**分类**](classification/README_zh-CN.md)
- [**检测**](detection/README_zh-CN.md)
- [**姿态**](pose/README_zh-CN.md)

如果您需要特定场景下特定数据集的预训练模型，欢迎向我们[提交 Issues](https://github.com/Seeed-Studio/sscma-model-zoo/issues/new/choose)。

## 快速上手

如果您希望使用 SSCMA Model Zoo 提供的模型，我们建议您遵循以下步骤:

1. 根据实际需求，选择相应的应用场景并挑选合适的神经网络。您可以浏览我们给出的测试数据进行选择。
2. 下载选择好的模型。对于公开的预训练模型，您可以通过测试数据表格中的模型链接直接下载。
3. 参考 [SSCMA 文档 - 部署示例](https://sensecraftma.seeed.cc/SSCMA/zh_cn/examples/examples)在边缘计算设备上进行部署。您也可以使用 SSCMA 在您的计算机上运行我们的模型，对我们的测试结果进行复现或推理测试。

## Device

目前模型通过测试的有以下设备，其中推理时间则是根据对应设备实际测试的结果（包含前处理以及后处理）

- <sup>1</sup> [ESP32-S3 (XIAO)](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/).

- <sup>2</sup> [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/).

- <sup>3</sup> [SenseCAP A1101](https://wiki.seeedstudio.com/SenseCAP-Vision-AI-Get-Started/).

## 故障排除

如果您在使用 SSCMA Model Zoo 中预训练模型时遇到任何问题，我们建议您先按照以下步骤排查:

1. 检查下载模型的正确性。预训练模型文件名的末尾包含该模型的 SHA-1 哈希值，您可以自行计算下载模型的 SHA-1 并与模型文件名中的进行比对 (如使用 Linux 下的 `sha1sum` 命令)，校验模型一致性。
2. 搜索 [SSCMA Model Zoo - Issues](https://github.com/Seeed-Studio/sscma-model-zoo/issues) 和 [SSCMA - Issues](https://github.com/Seeed-Studio/SSCMA/issues)，浏览是否有其他人反馈类似的问题。

如果以上方法都不能起到帮助，或者有其他关于 SSCMA Model Zoo 的问题，请向我们[提交 Issues](https://github.com/Seeed-Studio/sscma-model-zoo/issues/new/choose)。

## 开源许可证

不同的神经网络、数据集和模型受不同的开园许可证保护，具体请参考 [LICENSES](LICENSES)。
