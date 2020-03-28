import cv2
import image_saver
import image_detector
import time


class ImageTaker(object):
    def __init__(self,
                 image_saver: image_saver.ImageSaver,
                 image_detector: image_detector.ImageDetector):
        self._image_saver = image_saver
        self._image_detector = image_detector

    def run(self,
            localtime: time.struct_time,
            save_image: bool,
            save_detection: bool):
        video = cv2.VideoCapture(0)
        if not video.isOpened():
            print('ImageTaker : カメラを開けなかった。')
            return
        ret, image = video.read()
        video.release()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if save_image:
            self._image_saver.save_image(localtime=localtime, image=image)
        self._image_detector.detect(localtime=localtime, image=image, save_detection=save_detection)
