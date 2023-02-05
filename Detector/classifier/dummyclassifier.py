from .classifier import Classifier
from .classifyresult import ClassifyResult
from typing import List


class DummyClassifier(Classifier):
    def classify_from_single_pil(self, image_pil) -> ClassifyResult:
        return ClassifyResult(
            2,
            0.2, 0.3, 0.5
        )

    def classify_from_multiple_pil(self, image_pil_s) -> List[ClassifyResult]:
        return [self.classify_from_single_pil()]

    def classify_from_single_tensor(self, image_tensor) -> ClassifyResult:
        return self.classify_from_single_pil()

    def classify_from_multiple_tensor(self, image_s_tensor) -> List[ClassifyResult]:
        return self.classify_from_multiple_pil()
