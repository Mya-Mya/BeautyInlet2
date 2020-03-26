import cv2
import numpy as np
import image_saver
import image_detector


class ImageTaker(object):
    def __init__(self,
                 image_saver: image_saver.ImageSaver,
                 image_detector: image_detector.ImageDetector):
        self._image_saver = image_saver
        self._image_detector = image_detector

    def run(self, save_image: bool, detect_image: bool):
        video = cv2.VideoCapture(0)
        if not video.isOpened():
            print('image_taker.take_image : カメラを開けなかった。')
            return
        ret, image = video.read()
        video.release()

        if save_image:
            self._image_saver.save_image(image)
        if detect_image:
            self._image_detector.save_detection(image)
