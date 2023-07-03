# Classification Overview

The classification model zoo includs several pre-trained models from different optimized neural networks which trained using [EdgeLab](https://github.com/Seeed-Studio/EdgeLab).

The hierarchy of detection directory is as follows:

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

The `models` folder includes different neural networks, each neural network is denoted as its name, located on `<network name>` folder. Inside the neural network folder, the model may trained on different datasets, so we use the `<datasets name>` to to partition these pre-trained models into different folders.


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

*Note:*


<sup>1</sup> Measured on [ESP32-S3 (XIAO)](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/).

<sup>2</sup> Measured on [Grove Vision AI](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/).

<sup>3</sup> Measured on [SenseCAP A1101](https://wiki.seeedstudio.com/SenseCAP-Vision-AI-Get-Started/).


