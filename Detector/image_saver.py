import setting_manager
import numpy as np
from PIL import Image
import time
import os


class ImageSaver(object):
    def __init__(self, setting_manager: setting_manager.SettingManager):
        self._setting_manager = setting_manager

    def save_image(self,localtime:time.struct_time, image: np.ndarray):
        image_pil = Image.fromarray(image)
        dir = self._setting_manager.get_image_save_dir()
        fname='{}_{:02d}_{:02d}_{:02d}_{:02d}_{:02d}.jpg'.format(
            localtime.tm_year,
            localtime.tm_mon,
            localtime.tm_mday,
            localtime.tm_hour,
            localtime.tm_min,
            localtime.tm_sec
        )
        fp = os.path.join(dir, fname)
        image_pil.save(fp)
        print('ImageSaver : I saved the image to {}'.format(fp))
