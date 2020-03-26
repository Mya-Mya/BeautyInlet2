import setting_manager
import numpy as np
import threading


class ImageDetector(object):
    def __init__(self, setting_manager: setting_manager.SettingManager):
        self._setting_manager = setting_manager

    def save_detection(self, image: np.ndarray):
        print('Detector.save_detection')
