# Pose Overview

The pose model zoo includs several pre-trained models from different optimized neural networks which trained using [EdgeLab](https://github.com/Seeed-Studio/EdgeLab).

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

### PFLD MoblieNetV2

| Model Name | Backend | Datasets | Input Size | ACC | MACs (M) | Parameters (M) | Invoking RAM (MiB) | Invoke Time (ms) | Link |
|--|--|--|--|--|--|--|--|--|--|
| pfld_mobilenetv2 | PyTorch | WFLW | 112x112x3 | TODO | TODO | TODO | TODO | TODO| [Download Github](TODO)|

## Example of Models

The section shows the example of models trained from different datasets.

### PFLD MoblieNetV2

| Model Name | Backend | Datasets | Input Size | ACC | Invoke Time (ms) | Link |
|--|--|--|--|--|--|--|
| pfld_mobilenetv2 | PyTorch | [pointer meter](TODO) | 112x112x3 | TODO | TODO | [Download Github](TODO)|


