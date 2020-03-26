import setting_manager
import numpy as np
import threading
import os


class ImageDetector(object):
    def __init__(self,
                 setting_manager: setting_manager.SettingManager):
        self._setting_manager = setting_manager
        self._loader = threading.Thread(target=self.load_tf_and_detection_model)
        self._loader.start()

    def load_tf_and_detection_model(self):
        print('ImageDetector.__init__ TensorFlow及び検出モデルの読み込み中。')
        import tensorflow as tf
        my_dir = os.path.dirname(__file__)
        self._model = tf.keras.models.load_model(os.path.join(my_dir, "..", "modelF_for_1.4-00300.h5"))

    def save_detection(self, image: np.ndarray):
        if self._loader.is_alive():
            print('ImageDetector.save_detection : 未だTensorFlow及び検出モデルの読み込み中。お待ちを。')
            self._loader.join()
        print('Detector.save_detection')
