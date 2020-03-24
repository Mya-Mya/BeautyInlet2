import json
import os
try:
    with open('nothing')as f:
        print(f)
except:
    print('ありません')

class SettingManager(object):
    '''BeautyInlet2の設定ファイルを読み書きする。'''
    def __init__(self):
        self._my_dir=os.path.dirname(__file__)
        self._setting_fname=os.path.join(self._my_dir,'..','test_text.txt')
        self._setting={}
        self.restore_default_setting()

    def create_new_setting_file(self):
        pass
    def restore_default_setting(self):
        self.set_image_save_dir(os.path.join(self._my_dir,'..','default_image_save_dir'))
        self.set_seeninfo_save_dir(os.path.join(self._my_dir,'..','default_seeninfo_save_dir'))
        self.set_taking_image_plans([])
    def write_setting(self):
        pass

    def get_image_save_dir(self):
        return self._setting['imageSaveDir']
    def set_image_save_dir(self,d):
        self._setting['imageSaveDir']=d

    def get_seeninfo_save_dir(self):
        return self._setting['seeninfoSaveDir']
    def set_seeninfo_save_dir(self,d):
        self._setting['seeninfoSaveDir']=d

    def get_taking_image_plans(self):
        return self._setting['takingImagePlans']
    def set_taking_image_plans(self,p):
        self._setting['takingImagePlans']=p
    def add_or_edit_taking_image_plan(self,h,m,save_image,save_seeninfo):
        pass
    def delete_taking_image_plan(self,h,m):
        pass