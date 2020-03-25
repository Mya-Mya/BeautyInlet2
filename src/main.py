import threading
import setting_manager
import bi2command
import bi2info
import timekeeper
import os

def exit_immediately():
    inst_setting_manager.save_setting()
    os._exit(0)

print('{} ({}) 〜{}〜\n{}'.format(
    bi2info.NAME,
    bi2info.FULL_VERSION,
    bi2info.SUBTITLE,
    bi2info.COPYRIGHT
))

inst_setting_manager = setting_manager.SettingManager()

time_keeper=timekeeper.TimeKeeper(
    setting_manager=inst_setting_manager
)
thread_time_keeper=threading.Thread(target=time_keeper.run)

inst_bi2command=bi2command.BI2Command(
    setting_manager=inst_setting_manager,
    exit_func=exit_immediately
)
thread_bi2command=threading.Thread(target=inst_bi2command.cmdloop)
thread_bi2command.setDaemon(True)

thread_time_keeper.start()
thread_bi2command.start()