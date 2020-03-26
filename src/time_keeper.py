import time
import threading
import setting_manager
import image_taker


class TimeKeeper(object):
    def __init__(self,
                 setting_manager: setting_manager.SettingManager,
                 image_taker: image_taker.ImageTaker,
                 end_event: threading.Event):
        self._setting_manager = setting_manager
        self._image_taker = image_taker
        self._end_event = end_event

    def run(self):
        while True:
            time.sleep(1)
            localtime = time.localtime()
            if localtime.tm_sec is not 0: continue

            # 毎分0秒にチェックを実施する
            tm_hour = localtime.tm_hour
            tm_min = localtime.tm_min

            # 終了時刻のチェック
            exit_h, exit_m = self._setting_manager.get_exit_time()
            if exit_h is tm_hour and exit_m is tm_min:
                self._end_event.set()

            # 撮影計画のチェック
            for plan in self._setting_manager.get_taking_plans():
                if plan['h'] is tm_hour and plan['m'] is tm_min:
                    self._image_taker.run(plan['saveImage'], plan['saveDetection'])
