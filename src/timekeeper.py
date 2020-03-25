import time
import setting_manager

class TimeKeeper(object):
    def __init__(self, setting_manager:setting_manager.SettingManager):
        self._setting_manager=setting_manager
    def run(self):
        while True:
            time.sleep(1)
            localtime=time.localtime()
            if localtime.tm_sec is not 0:continue

            #毎分0秒にチェックを実施する
            tm_hour=localtime.tm_hour
            tm_min=localtime.tm_min
            for plan in self._setting_manager.get_taking_plans():
                if plan['h']is tm_hour and plan['m']is tm_min:
                    print('お仕事の時間でぇぇぇぇす！！！')
                    print(plan)
