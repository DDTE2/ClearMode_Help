from os.path import abspath
from os import remove, walk
from shutil import rmtree
from json import dumps, loads
from sqlite3 import connect


# ����� �������� ������ ������������
class Clear:
    def __init__(self):
        # ���������� ���� � ����� � �������
        path = abspath(__file__).split('\\')[:-2]
        self.path = '\\'.join(path + ['data'])

        # ������� �����
        self.Delite_Files()
        # ������ ����
        self.Clear_Cookies()

    def Delite_Files(self):  # ������� ������ �����
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

    def Clear_Cookies(self):  # ������ ����
        # ������������ � ����� ����
        db = connect(self.path + '/cookies.sqlite')

        # ������ SessionId
        db.execute(
            "UPDATE moz_cookies SET value = '', expiry = 0, lastAccessed = 0, creationTime = 0 WHERE name = 'SessionId'")

        # ��������� ���� ����
        db.commit()


Clear()