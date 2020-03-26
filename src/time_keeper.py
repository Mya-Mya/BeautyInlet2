import time
import threading
import setting_manager

class TimeKeeper(object):
    def __init__(self, setting_manager:setting_manager.SettingManager, end_event:threading.Event):
        self._setting_manager=setting_manager
        self._end_event=end_event
    def run(self):
        while True:
            time.sleep(1)
            localtime=time.localtime()
            if localtime.tm_sec is not 0:continue

            #毎分0秒にチェックを実施する
            tm_hour=localtime.tm_hour
            tm_min=localtime.tm_min

            exit_h,exit_m=self._setting_manager.get_exit_time()
            if exit_h is tm_hour and exit_m is tm_min:
                self._end_event.set()

            for plan in self._setting_manager.get_taking_plans():
                if plan['h']is tm_hour and plan['m']is tm_min:
                    print('お仕事の時間でぇぇぇぇす！！！')
                    print(plan)