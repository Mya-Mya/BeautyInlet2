from pathlib import Path
from typing import List
import tensorflow
from tensorflow import Tensor as TFTensor
from PIL.Image import Image as PILImage
from dataclasses import dataclass


@dataclass
class ClassifyResult:
    label: int
    unclear_score: float
    notseen_score: float
    seen_score: float


UNCLEAR = 0
NOTSEEN = 1
SEEN = 2

IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS = 120, 160, 3
IMG_DTYPE = tensorflow.float32


class Classifier():
    def __init__(self, model_fp: Path) -> None:
        self.model: tensorflow.keras.models.Model = \
            tensorflow.keras.models.load_model(str(model_fp))
        assert self.model.input_shape == \
            (None, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS)
        assert self.model.output_shape == (None, IMG_CHANNELS)

    def convert_imagepil_to_imagetensor(self, image_pil: PILImage) -> TFTensor:
        image_pil_resized = image_pil.resize((IMG_WIDTH, IMG_HEIGHT)) \
            if not image_pil.size == (IMG_WIDTH, IMG_HEIGHT)\
            else image_pil
        image_tensor = tensorflow.constant(
            image_pil_resized, dtype=IMG_DTYPE)/255.
        return image_tensor

    def classify_from_single_pil(self, image_pil: PILImage) -> ClassifyResult:
        image_tensor = self.convert_imagepil_to_imagetensor(image_pil)
        return self.classify_from_single_tensor(image_tensor)

    def classify_from_multiple_pil(self, image_pil_s: List[PILImage]) -> List[ClassifyResult]:
        image_tensor_s = list(map(
            self.convert_imagepil_to_imagetensor, image_pil_s
        ))
        image_s_tensor = tensorflow.stack(image_tensor_s)
        return self.classify_from_multiple_tensor(image_s_tensor)

    def classify_from_single_tensor(self, image_tensor: TFTensor) -> ClassifyResult:
        assert image_tensor.shape == (IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS)
        assert image_tensor.dtype == IMG_DTYPE
        image_s_tensor = image_tensor[None, :]
        return self.classify_from_multiple_tensor(image_s_tensor)[0]

    def classify_from_multiple_tensor(self, image_s_tensor: TFTensor) -> List[ClassifyResult]:
        assert len(image_s_tensor.shape) == 4
        assert image_s_tensor.shape[1:] == \
            (IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS)
        output = self.model(image_s_tensor)

        classifyresult_s = []
        label_s = tensorflow.argmax(output, axis=1).numpy()
        for label, scores in zip(label_s, output.numpy()):
            classifyresult = ClassifyResult(
                label=label,
                unclear_score=scores[0],
                notseen_score=scores[1],
                seen_score=scores[2]
            )
            classifyresult_s.append(classifyresult)
        return classifyresult_s
