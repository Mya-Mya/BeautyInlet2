import setting_manager
import numpy as np
from PIL import Image
import time
import os


class ImageSaver(object):
    def __init__(self, setting_manager: setting_manager.SettingManager):
        self._setting_manager = setting_manager

    def save_image(self, image: np.ndarray):
        image_pil = Image.fromarray(image)
        fname = time.strftime('%Y_%m_%d_%H_%M_%S.jpg')
        dir = self._setting_manager.get_image_save_dir()
        fp = os.path.join(dir, fname)
        image_pil.save(fp)
        print('ImageSaver.save_image : {}を保存した'.format(fp))
