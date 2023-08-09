# Работа с файлами
from os.path import expanduser, normpath, abspath
from os import remove
from win32com.client import Dispatch
# Название OS
from sys import platform
# Формат данных
from json import dumps


class Shortcut:
    def __init__(self):
        self.project_name = 'main.py'
        if not self.getPaths():
            pass

    def getPaths(self):
        # Определяем путь к рабочему столу
        try:
            self.desktop = expanduser("~/Desktop")
        except:
            try:
                # the above is valid on Windows (after 7) but if you want it in os normalized form:
                self.desktop = normpath(expanduser("~/Desktop"))
            except:
                return 'DesktopError'

        # Определяем путь к исполняемому файлу
        path = abspath(__file__).split('\\')[:-2]
        self.path = '\\'.join(path + [self.project_name])

        return None

    def Create(self):  # Функция создания ярлыка
        if not self.Check_Shortcut():
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(self.desktop + '/Clear Mod.lnk')
            shortcut.TargetPath = self.path
            shortcut.Arguments = '/cmd {%s} -new_console' % 'Clear Mod.lnk'
            shortcut.WorkingDirectory = self.desktop
            shortcut.save()

    def Delete(self):  # Функция удаления ярлыка
        if self.Check_Shortcut():
            remove(self.desktop + '/Clear Mod.lnk')

    def Check_Shortcut(self):  # Проверяем, ни создан ли уже ярлык
        try:
            with open(self.desktop + '\\Clear Mod.lnk', 'rb') as file:
                pass
            return True
        except:
            return False

    def Check_System(self):  # Проверяем название опрационной системы
        if platform == 'win32':
            return True
        else:
            return False

    def __str__(self):
        data = self.__dict__
        data['win'] = self.Check_System()
        data['isCreate'] = self.Check_Shortcut()

        return dumps(data, ensure_ascii=False, indent=4)
