from typing import List, Optional
from threading import Thread
from PIL import Image
from datetime import datetime

from camera import Camera
from classifier import Classifier, ClassifyResult, IMG_WIDTH, IMG_HEIGHT
from detectionsaver import DetectionSaver
from imagesaver import ImageSaver
from datetime import datetime
from takefirerer import TakeFierer


class BI2DetectorApp():
    def __init__(self,
                 classifier: Classifier,
                 camera: Camera,
                 detectionsavers: List[DetectionSaver],
                 imagesavers: List[ImageSaver],
                 takefierers: List[TakeFierer]
                 ) -> None:
        self.classifier = classifier
        self.camera = camera
        self.detectionsavers = detectionsavers
        self.imagesavers = imagesavers
        self.takefierers = takefierers

        for takefierer in takefierers:
            thread = Thread(
                target=takefierer.run, 
                args=[lambda:self.take_image()], 
                daemon=True
            )
            thread.start()

    def justify_image(self, image: Image.Image) -> Image.Image:
        image = image.convert("RGB")

        ratio = max(float(IMG_HEIGHT)/float(image.height),
                    float(IMG_WIDTH)/float(image.width))
        image = image.resize((int(image.width*ratio), int(image.height*ratio)))

        left = max(0, int(0.5*(image.width-IMG_WIDTH)))
        upper = max(0, int(0.5*(image.height-IMG_HEIGHT)))
        image = image.crop((left, upper, left+IMG_WIDTH, upper+IMG_HEIGHT))
        return image

    def take_image(self,
                   save_image: bool = True,
                   save_detection: bool = True,
                   date:Optional[datetime]=None
                   ):
        if (not save_image) and (not save_detection):
            return
        image = self.camera.take()
        image = self.justify_image(image)
        date = date or datetime.now()
        date_iso = date.isoformat()
        if save_image:
            for imagesaver in self.imagesavers:
                imagesaver.save(date_iso, image)
        if save_detection:
            classificationresult = self.classifier.\
                classify_from_single_pil(image)
            for detectionsaver in self.detectionsavers:
                detectionsaver.save(date_iso, classificationresult)
