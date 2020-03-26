import threading
import setting_manager
import bi2command
import bi2info
import time_keeper
import sys

end_event=threading.Event()

def wait_for_end():
    global end_event,inst_setting_manager
    end_event.wait()
    inst_setting_manager.save_setting()
    print('Bye')
    sys.exit(0)

print('{} ({}) 〜{}〜\n{}\n'.format(
    bi2info.NAME,
    bi2info.FULL_VERSION,
    bi2info.SUBTITLE,
    bi2info.COPYRIGHT
))

# 設定管理
inst_setting_manager = setting_manager.SettingManager()

# 時間管理
time_keeper = time_keeper.TimeKeeper(
    setting_manager=inst_setting_manager,
    end_event=end_event
)
thread_time_keeper = threading.Thread(target=time_keeper.run)
thread_time_keeper.setDaemon(True)

# コマンド受付
inst_bi2command = bi2command.BI2Command(
    setting_manager=inst_setting_manager,
    end_event=end_event
)
thread_bi2command = threading.Thread(target=inst_bi2command.cmdloop)
thread_bi2command.setDaemon(True)

# デーモンスレッドの開始
thread_time_keeper.start()
thread_bi2command.start()

# 終了業務
thread_wait_for_end=threading.Thread(target=wait_for_end)

# 通常スレッドの開始
thread_wait_for_end.start()