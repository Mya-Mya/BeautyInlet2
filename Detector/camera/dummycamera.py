from .camera import Camera
from tkinter import filedialog
from PIL import Image


class DummyCamera(Camera):
    def take(self) -> Image.Image:
        fp = filedialog.askopenfilename(title="Choose image to return.")
        image = Image.open(fp)
        return image
