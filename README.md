# Seed Studio EdgeLab Model Zoo

<div align="center">
  <img width="100%" src="https://cdn.jsdelivr.net/gh/Seeed-Studio/EdgeLab@main/docs/public/images/EdgeLab-Logo.png">
</div>

English | [简体中文](README_zh-CN.md)


## Introduction

Welcome to Seed Studio EdgeLab Model Zoo. We provide a series of pre-trained models for different application scenarios for you to use, with [Seed Studio EdgeLab](https://github.com/Seeed-Studio/EdgeLab), you can test or inference on these models and easily deploy them to edge computing devices.

EdgeLab Model Zoo focuses on providing models trained on EdgeLab optimized neural networks, which are tailored to real-world application scenarios and enable faster and more accurate inference on embedded devices.


## Application Scenario

Currently, EdgeLab Model Zoo provides pre-trained models for the following application scenarios:

- [Classification](classification/README.md)
- [Detection](detection/README.md)
- [Pose](pose/README.md)

If you need any pre-trained model for a specific dataset in a specific scenario, feel free to submit a feature request to [Issues](https://github.com/Seeed-Studio/edgelab-model-zoo/issues/new/choose).

## Quickly Start

If you wish to use the model provided by EdgeLab Model Zoo, we recommend that you follow the following steps:

1. Based on actual needs, select corresponding application scenario and choose appropriate neural networks. You can browse the test results that we provide for dicision.
2. Download the selected pre-trained model. For public pre-trained models, you can directly download them through the model link in the test results table.
3. Please refer to [EdgeLab Documentation - Deployment Example](https://seeed-studio.github.io/EdgeLab/examples/examples) to deploy on edge computing devices. You can also use EdgeLab to run our models on your computer, reproduce our test results or infer directly.


## Troubleshooting

If you encounter any problem with pre-trained models in EdgeLab Model Zoo, we recommend that you first follow these steps to troubleshoot.

1. Check the correctness of the downloaded model. The end of the pre-trained model file name contains the SHA-1 hash of the model. You can calculate the SHA-1 of the downloaded model and compare it with the one in the model file name by yourself (e.g. using the `sha1sum` command under Linux) to check the model consistency.
2. Search [EdgeLab Model Zoo - Issues](https://github.com/Seeed-Studio/edgelab-model-zoo/issues) and [EdgeLab - Issues](https://github.com/Seeed-Studio/EdgeLab/issues) to see if there are other people who have the similar problem.

If none of the above methods help, or if you have other questions about EdgeLab Model Zoo, please [Submit Issues](https://github.com/Seeed-Studio/edgelab-model-zoo/issues/new/choose) to us.


## License

Different neural networks, datasets, and models are protected by different licenses, please refer to the [LICENSES](LICENSES) for detailed permissions and restrictions.
