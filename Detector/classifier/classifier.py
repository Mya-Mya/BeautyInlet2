from typing import List
from abc import ABC, abstractmethod
from .classifyresult import ClassifyResult


class Classifier(ABC):
    @abstractmethod
    def classify_from_single_pil(self, image_pil) -> ClassifyResult:
        pass

    @abstractmethod
    def classify_from_multiple_pil(self, image_pil_s) -> List[ClassifyResult]:
        pass

    @abstractmethod
    def classify_from_single_tensor(self, image_tensor) -> ClassifyResult:
        pass

    @abstractmethod
    def classify_from_multiple_tensor(self, image_s_tensor) -> List[ClassifyResult]:
        pass
