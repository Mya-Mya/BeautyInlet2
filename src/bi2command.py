import cmd
import threading
import time

import setting_manager
import bi2info
import image_taker


class BI2Command(cmd.Cmd):
    prompt = 'BI2cmd : '
    doc_header = bi2info.DESCRIPTION
    ruler = '-'

    def __init__(self,
                 setting_manager: setting_manager.SettingManager,
                 image_taker: image_taker.ImageTaker,
                 end_event: threading.Event):
        super().__init__()
        self._setting_manager = setting_manager
        self._image_taker = image_taker
        self._end_event = end_event

    def default(self, line):
        print('Unknown Command')

    def to_four_digit_time(self, h: int, m: int) -> str:
        return '{:02d}{:02d}'.format(h, m)

    def to_hour_and_minuite(self, four_digit_date: str) -> tuple:
        h = int(four_digit_date[0:2])
        m = int(four_digit_date[2:4])
        return (h, m)

    def do_showplans(self, arg):
        '''撮影計画の一覧を表示する。'''
        plan_list = self._setting_manager.get_taking_plans()
        print('{} Plan(s)'.format(len(plan_list)))
        for plan in plan_list:
            time = self.to_four_digit_time(plan['h'], plan['m'])
            print(time, end=' ')
            if plan['saveImage']: print('save image', end=' ')
            if plan['saveDetection']: print('save detection', end=' ')
            print('')

    def do_tidyplans(self, arg):
        '''撮影計画を時刻昇順に並べ替える。これを呼ばなくとも、次回起動時までに並べ替えはされる。'''
        self._setting_manager.tidy_taking_plans()

    def do_delplan(self, arg):
        '''撮影計画を削除する。argには削除するものの動作時刻を4桁で示す。
        4:15の撮影計画を削除する際は arg="0415"'''
        if len(arg) is not 4:
            print('type 4 letters in arg.')
        h, m = self.to_hour_and_minuite(arg)
        self._setting_manager.delete_taking_plan(h, m)

    def do_plan(self, arg):
        '''撮影計画を追加または上書きする。argには動作時刻を4桁で示した後、画像を保存する場合はi、識別を保存する場合はdを追加する。
        15:0に保存と識別をする撮影計画を追加/上書きする際は arg="1500id"
        10:10に識別をする撮影計画を追加/上書きする際は arg="1010d"'''
        if len(arg) < 4:
            print('type 4 or more letters in arg.')
        h, m = self.to_hour_and_minuite(arg[0:4])
        params = arg[4:len(arg)]
        save_image = ('i' in params)
        save_detection = ('d' in params)
        self._setting_manager.add_or_edit_taking_plan(h, m, save_image, save_detection)

    def do_p(self, arg):
        '''planと同じ。'''
        self.do_plan(arg)

    def do_take(self, arg):
        '''今すぐ撮影し識別する。argには画像を保存する場合はi、識別を保存する場合はdを追加する。'''
        self._image_taker.run(
            localtime=time.localtime(),
            save_image='i' in arg,
            save_detection='d' in arg
        )

    def do_showsettingdirs(self, arg):
        '''撮影した画像、検出情報の保存先ディレクトリを表示する。'''
        print('Images are saved to : ', end='')
        print(self._setting_manager.get_image_save_dir())
        print('Detections are saved to : ', end='')
        print(self._setting_manager.get_detection_save_dir())

    def do_savingimgdir(self, arg):
        '''撮影した画像の保存先ディレクトリを指定する。'''
        self._setting_manager.set_image_save_dir(arg)

    def do_savingdetectiondir(self, arg):
        '''検出情報の保存先ディレクトリを指定する。'''
        self._setting_manager.set_detection_save_dir(arg)

    def do_showexittime(self, arg):
        '''終了時刻を表示する。'''
        h, m = self._setting_manager.get_exit_time()
        print('I`ll exit on {:02d}:{:02d}.'.format(h, m))

    def do_exittime(self, arg):
        '''終了時刻を argに4桁で示す。
        2:0に終了する場合は arg="0200"'''
        if len(arg) is not 4:
            print('type 4 letters in arg.')
            return
        h, m = self.to_hour_and_minuite(arg)
        self._setting_manager.set_exit_time(h, m)

    def do_exit(self, arg):
        '''BeautyInlet2を終了する。'''
        self._end_event.set()
