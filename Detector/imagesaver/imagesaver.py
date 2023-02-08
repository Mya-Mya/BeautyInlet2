from PIL import Image
from abc import ABC, abstractmethod


class ImageSaver(ABC):
    @abstractmethod
    def save(self, date_iso: str, image: Image.Image) -> None:
        pass
