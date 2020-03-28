import csv

import setting_manager
import numpy as np
import threading
import os
import time
import glob

IMG_HEIGHT,IMG_WIDTH=120,160

class ImageDetector(object):
    def __init__(self,
                 setting_manager: setting_manager.SettingManager):
        self._setting_manager = setting_manager
        self._loader = threading.Thread(target=self.load_tf_and_detection_model)
        self._loader.start()

    def load_tf_and_detection_model(self):
        print('ImageDetector : TensorFlow及び検出モデルの読み込み中。')
        import tensorflow as tf
        my_dir = os.path.dirname(__file__)
        self._model = tf.keras.models.load_model(os.path.join(my_dir, "..", "modelA-01500.h5"))
        print('ImageDetector : TensorFlow及び検出モデルの読み込み完了。')

    def detect(self, localtime: time.struct_time, image: np.ndarray, save_detection: bool):
        if self._loader.is_alive():
            print('ImageDetector.save_detection : 未だTensorFlow及び検出モデルの読み込み中。お待ちを。')
            self._loader.join()
        print('Detector.detect')
        if save_detection:
            self.save_detection(localtime=localtime,detection='未観測')

    def save_detection(self, localtime: time.struct_time, detection: str):
        dir = self._setting_manager.get_detection_save_dir()
        fname = '{}_{:02d}.csv'.format(localtime.tm_year, localtime.tm_mon)
        filepath = os.path.join(dir, fname)
        fieldnames = ['year', 'mon', 'day', 'hour', 'min', 'sec', 'detection']
        exists = (glob.glob(filepath) is not [])
        with open(filepath, 'a')as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not exists:
                writer.writeheader()
            writer.writerow({
                'year': localtime.tm_year,
                'mon': localtime.tm_mon,
                'day': localtime.tm_mday,
                'hour': localtime.tm_hour,
                'min': localtime.tm_min,
                'sec': localtime.tm_sec,
                'detection': detection
            })
