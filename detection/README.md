# Detection Overview

The object detection model zoo includs several pre-trained models from different optimized neural networks which trained using [SSCMA](https://github.com/Seeed-Studio/SSCMA).

The hierarchy of detection directory is as follows:

```txt
type
├── <datasets name>
│   ├── <pre-trained model>
│   └── ...
└── ...
```

## Task

At present, the following devices have passed the test of the model, and the inference time is based on the actual test results of the corresponding devices (including pre-processing and post-processing)

- [FACE](./face/README.md)
- [METER](./meter/README.md)
- [PERSON](./person/README.md)
