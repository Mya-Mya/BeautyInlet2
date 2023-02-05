from .detectionsaver import DetectionSaver
from classifier import ClassifyResult


class EchoDetectionSaver(DetectionSaver):
    def save(self, date_iso: str, result: ClassifyResult):
        print("EchoDetectionSaver#save")
        print(f"date_iso={date_iso} result={result}")
