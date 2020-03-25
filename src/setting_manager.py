import json
import os
import io
from operator import itemgetter


class SettingManager(object):
    '''BeautyInlet2の設定ファイルを読み書きする。'''

    def __init__(self):
        self._my_dir = os.path.dirname(__file__)
        self._setting_fname = os.path.join(self._my_dir, '..', 'setting.json')
        self.restore_default_setting()
        try:
            with io.open(self._setting_fname)as f:
                self._setting=json.load(f)
        except:
            pass

    def restore_default_setting(self):
        self._setting={}
        self.set_image_save_dir(os.path.join(self._my_dir, '..', 'default_image_save_dir'))
        self.set_detection_save_dir(os.path.join(self._my_dir, '..', 'default_seeninfo_save_dir'))
        self.set_taking_plans([])

    def get_image_save_dir(self)->str:
        return self._setting['imageSaveDir']

    def set_image_save_dir(self, d:str):
        self._setting['imageSaveDir'] = d

    def get_detection_save_dir(self)->str:
        return self._setting['detectionSaveDir']

    def set_detection_save_dir(self, d:str):
        self._setting['detectionSaveDir'] = d

    def get_taking_plans(self)->list:
        return self._setting['takingPlans']

    def set_taking_plans(self, p:list):
        self._setting['takingPlans'] = p

    def add_or_edit_taking_plan(self, h:int, m:int, save_image:bool, save_detection:bool):
        # 同じ時刻の撮影計画が既にあればそれを一度削除する。
        self.delete_taking_plan(h,m)
        # 撮影計画を追加する。
        self._setting['takingPlans'].append({
            'h':h,
            'm':m,
            'saveImage':save_image,
            'saveDetection':save_detection
        })

    def delete_taking_plan(self, h:int, m:int):
        for plan in self._setting['takingPlans']:
            if plan['h']==h and plan['m']==m:
                self._setting['takingPlans'].remove(plan)

    def tidy_taking_plans(self):
        self.set_taking_plans(
            sorted(self.get_taking_plans(),key=itemgetter('h','m'))
        )

    def save_setting(self):
        self.tidy_taking_plans()
        with io.open (self._setting_fname,'w') as f:
            json.dump(self._setting, f, indent=1)

