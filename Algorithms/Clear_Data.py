from os.path import abspath
from os import remove, walk
from shutil import rmtree
from json import dumps, loads
from sqlite3 import connect


# Класс отчистки данных пользователя
class Clear:
    def __init__(self):
        # Определяем путь к папке с данными
        path = abspath(__file__).split('\\')[:-2]
        self.path = '\\'.join(path + ['data'])

        # Удаляем файлы
        self.Delite_Files()
        # Чистим куки
        self.Clear_Cookies()

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


Clear()
