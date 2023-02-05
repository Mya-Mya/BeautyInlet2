from .camera import Camera
import cv2
from PIL import Image


class WebCamera(Camera):
    def take(self) -> Image.Image:
        vc: cv2.VideoCapture = cv2.VideoCapture(0)
        if not vc.isOpened():
            raise ValueError("WebCamera#take : Web Camera is not opened.")
        ret, image = vc.read()
        vc.release()
        if not ret:
            raise ValueError("WebCamera#take : Could not get the image.")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        return image
