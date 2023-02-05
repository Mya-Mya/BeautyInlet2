from .imagesaver import ImageSaver
from PIL import Image
from pathlib import Path
from datetime import datetime


class FileImageSaver(ImageSaver):
    def __init__(self, save_dir: Path) -> None:
        self.save_dir = save_dir

    def get_date_text(self, date_iso:str) -> str:
        date = datetime.fromisoformat(date_iso)
        date_text = f"{date.year}.{date.month:02d}.{date.day:02d}-{date.hour:02d}.{date.minute:02d}.{date.second:02d}"
        return date_text

    def save(self, date_iso: str, image: Image.Image) -> None:
        date_text = self.get_date_text(date_iso)
        fp = self.save_dir/date_text
        image.save(fp)