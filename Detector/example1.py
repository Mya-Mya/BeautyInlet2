from datetime import datetime
print("Import", datetime.now())

from bi2detectorapp import BI2DetectorApp

from classifier.tfclassifier import TFClassifier
from camera import WebCamera
from detectionsaver import EchoDetectionSaver, HttpDetectionSaver
from imagesaver import PreviewImageServer

from pathlib import Path

print("Launching TFClassifier", datetime.now())
classifier = TFClassifier(Path(__file__).parent/"models"/"B-00500.h5")
print("Launcing WebCamera", datetime.now())
camera = WebCamera()
print("Launcing Detection Savers", datetime.now())
detectionsavers = [EchoDetectionSaver(), HttpDetectionSaver()]
print("Launching PreviewImageServer", datetime.now())
imagesavers = [PreviewImageServer()]
print("Launching BI2DetectorApp", datetime.now())
app = BI2DetectorApp(
    classifier=classifier,
    camera=camera,
    detectionsavers=detectionsavers,
    imagesavers=imagesavers,
    takefierers=[]
)
print("Take", datetime.now())
app.take_image()
