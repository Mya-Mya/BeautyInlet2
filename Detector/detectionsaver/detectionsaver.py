from abc import ABC, abstractmethod
from classifier import ClassifyResult


class DetectionSaver(ABC):
    @abstractmethod
    def save(self, date_iso: str, result: ClassifyResult):
        pass
