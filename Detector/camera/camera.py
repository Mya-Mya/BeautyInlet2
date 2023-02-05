from abc import ABC, abstractmethod
from PIL import Image


class Camera(ABC):
    @abstractmethod
    def take(self) -> Image.Image:
        pass
