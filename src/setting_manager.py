import json
import os
import io
from operator import itemgetter
import bi2info
import platform

class SettingManager(object):
    '''BeautyInlet2の設定ファイルを読み書きする。'''

    def __init__(self):
        self._my_dir = os.path.dirname(__file__)
        setting_fname='setting-{}-{}.json'.format(bi2info.VERSION,platform.node())
        self._setting_full_fname = os.path.join(self._my_dir, '..', setting_fname)
        self.restore_default_setting()
        try:
            with io.open(self._setting_full_fname)as f:
                self._setting = json.load(f)
        except:
            print('SettingManager : {} was not found. I will create it on exit.'.format(self._setting_full_fname))
            pass

    def restore_default_setting(self):
        '''設定を初期状態に復元する。'''
        self._setting = {}
        self.set_exit_time(0, 0)
        self.set_image_save_dir(os.path.join(self._my_dir, '..', 'default_image_save_dir'))
        self.set_detection_save_dir(os.path.join(self._my_dir, '..', 'default_detection_save_dir'))
        self.set_taking_plans([])

    def get_exit_time(self) -> tuple:
        '''終了時刻を返す。'''
        time = self._setting['exitTime']
        return (time['h'], time['m'])

    def get_detection_save_dir(self) -> str:
        '''検出情報の保存先ディレクトリを返す。'''
        return self._setting['detectionSaveDir']

    def get_image_save_dir(self) -> str:
        '''撮影した画像の保存先ディレクトリを返す。'''
        return self._setting['imageSaveDir']

    def get_taking_plans(self) -> list:
        '''撮影計画を返す。'''
        return self._setting['takingPlans']

    def set_exit_time(self, h: int, m: int):
        '''終了時刻を指定する。'''
        self._setting['exitTime'] = {'h': h, 'm': m}

    def set_detection_save_dir(self, d: str):
        '''検出情報の保存先ディレクトリを指定する。'''
        self._setting['detectionSaveDir'] = d

    def set_image_save_dir(self, d: str):
        '''撮影した画像の保存先ディレクトリを指定する。'''
        self._setting['imageSaveDir'] = d

    def set_taking_plans(self, p: list):
        self._setting['takingPlans'] = p

    def add_or_edit_taking_plan(self, h: int, m: int, save_image: bool, save_detection: bool):
        '''撮影計画を追加または上書きする。'''
        # 同じ時刻の撮影計画が既にあればそれを一度削除する。
        self.delete_taking_plan(h, m)
        # 撮影計画を追加する。
        self._setting['takingPlans'].append({
            'h': h,
            'm': m,
            'saveImage': save_image,
            'saveDetection': save_detection
        })

    def delete_taking_plan(self, h: int, m: int):
        '''撮影計画を削除する。'''
        for plan in self._setting['takingPlans']:
            if plan['h'] == h and plan['m'] == m:
                self._setting['takingPlans'].remove(plan)

    def tidy_taking_plans(self):
        '''撮影計画を時刻昇順に並べ替える。'''
        self.set_taking_plans(
            sorted(self.get_taking_plans(), key=itemgetter('h', 'm'))
        )

    def save_setting(self):
        '''設定を書き込む。'''
        self.tidy_taking_plans()
        with io.open(self._setting_full_fname, 'w') as f:
            json.dump(self._setting, f, indent=1)
