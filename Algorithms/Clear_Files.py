from os.path import abspath
from os import remove, walk, getenv
from shutil import rmtree
from json import dumps, loads
from sqlite3 import connect
from Algorithms.ClearMod_run import ClearMod


# Класс отчистки данных пользователя
class ClearData:
    def __init__(self):
        # Определяем путь к папке с данными
        path = abspath(__file__).split('\\')[:-2]
        self.path = '\\'.join(path + ['data'])

        # Удаляем файлы Clear Mod
        CM = ClearMod()
        if not CM.isStarted():
            CM.Delete()

        self.Delite_Files()  # Удаляем данные
        self.Clear_Cookies()  # Чистим куки

    def Delite_Files(self):  # Удаляем лишние файлы
        for path, dirs, files in walk(self.path):
            for dir in dirs:
                try:
                    rmtree(path + '/' + dir)
                except:
                    pass
            for file in files:
                if file != 'cookies.sqlite':
                    try:
                        remove(path + '/' + file)
                    except:
                        pass

    def Clear_Cookies(self):  # Чистим куки
        # Подключаемся к файлу куки
        db = connect(self.path + '/cookies.sqlite')

        # Чистим SessionId
        db.execute(
            "UPDATE moz_cookies SET value = '', expiry = 0, lastAccessed = 0, creationTime = 0 WHERE name = 'SessionId'")

        # Сохраняем файл куки
        db.commit()
        db.close()


def ClearAppdata():
    appdata = getenv('APPDATA')

    for path, dirnames, filenames in walk(appdata):
        dir = path.split('\\')[-1].lower()
        if dir in ('adobe', 'mozilla', 'macromedia', 'shararam'):
            try:
                rmtree(path)
            except:
                pass
