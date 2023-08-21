# Classification Overview

The classification model zoo includs several pre-trained models from different optimized (Lighter and faster) neural networks which trained using [EdgeLab](https://github.com/Seeed-Studio/EdgeLab).

The hierarchy of detection directory is as follows:

```txt
classification
├── <datasets name>
│   ├── <pre-trained model>
│   └── ...
└── ...
```


## Task

The models are classified according to the target tasks, which is convenient for users to find model solutions suitable for their task requirements

- [CIFAR](./cifar/README.md)
- [MNIST](./mnist/README.md)
- [EMOTION](./emotion/README.md)
