from .detectionsaver import DetectionSaver
from classifier import ClassifyResult
from pathlib import Path
import requests
import json


class HttpDetectionSaver(DetectionSaver):
    def __init__(self) -> None:
        super().__init__()
        self.service_url = (
            Path(__file__).parent/".."/"Environments" /
            "detectiondbservice_url.txt"
        ).read_text

    def save(self, date_iso: str, result: ClassifyResult):
        requests.post(
            url=self.service_url,
            data=json.dumps({
                "dateISOString": date_iso,
                "statusLabel": result.label
            })
        )
