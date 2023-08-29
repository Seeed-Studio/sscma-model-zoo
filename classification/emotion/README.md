
### MobileNetV2 Rep

| Model Name | Backend | Input Size | Precision |Top-1(%) | Flops (M) | Param (M)  | Invoke Time (ms) | Link |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|MobileNetV2(0.35)  Rep| PyTorch | 48x48x1 | Float32 | 77.65 | 0.21 | 0.021 | - | [Download](https://files.seeedstudio.com/sscma/model_zoo/classification/models/emotion/mobilenetv2_1.0_rep_float32_sha1_63edb40ab3049449acc1ab9c4323d88916a8b81f.pth) |
|MobileNetV2(0.35) <> Rep| onnx | 48x48x1 | Float32 | 77.65 |  0.21 | 0.021 | - | [Download](https://files.seeedstudio.com/sscma/model_zoo/classification/models/emotion/mobilenetv2_1.0_rep_float32_sha1_913303ddb94f508bb8c7a88bf175a80936da7334.onnx) |
|MobileNetV2(0.35)  Rep| tflite | 48x48x1 | Float32 | 77.65 | 0.21 | 0.021 | - | [Download](https://files.seeedstudio.com/sscma/model_zoo/classification/models/emotion/mobilenetv2_1.0_rep_float32_sha1_163ae1113bd59724eb2848d59364667cdc09ae00.tflite) |
|MobileNetV2(0.35)  Rep| tflite | 48x48x1 | int8(PTQ) | 77.7 | 0.21 | 0.021 |  152<sup>(2)(3) | [Download](https://files.seeedstudio.com/sscma/model_zoo/classification/models/emotion/mobilenetv2_1.0_rep_int8_sha1_cf84f27f0e34cd85d64509346b09c510da969b6f.tflite) |
