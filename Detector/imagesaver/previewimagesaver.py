from .imagesaver import ImageSaver
from PIL import Image

class PreviewImageServer(ImageSaver):
    def save(self, date_iso: str, image: Image.Image) -> None:
        image.show(title=date_iso)