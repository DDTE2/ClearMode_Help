from random import choice, randint
from json import dumps
from sqlite3 import connect
from requests import post
from os.path import abspath
from hashlib import md5


class Registration:
    def __init__(self, name='', password='', referal='', avartar=0):
        self.name = name
        self.password = password
        self.referal = referal
        self.avartar = avartar

    def get_RandomUser(self):
        self.name = self.RandomStr_gen(symbols='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                       lenght=randint(4, 12))
        self.password = self.RandomStr_gen(
            symbols='!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё',
            lenght=12)

    def RandomStr_gen(self, symbols='', lenght=4):
        res = ''

        while lenght:
            res += choice(symbols)
            lenght -= 1

        return res

    def __str__(self):
        return dumps(self.__dict__, ensure_ascii=False)

    def Registration(self):
        url = 'https://www.shararam.ru/async/Register'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Shararam/2.0.3 Chrome/80.0.3987.165 Electron/8.2.5 Safari/537.36'}

        data = {'login': self.name,
                'password': self.password,
                'avatarid': self.avartar,
                'email': '',
                'referalName': self.referal}

        result = post(url, headers=headers, json=data)
        cookie = result.cookies.get_dict()
        Coockes(cookie['SessionId']).SaveCoockie()


class Authorization:
    def __init__(self, name='', password=''):
        self.name = name
        self.password = password

    def Check_Name(self):
        url = 'https://www.shararam.ru/api/user/check_login'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Shararam/2.0.3 Chrome/80.0.3987.165 Electron/8.2.5 Safari/537.36'}

        data = {'login': self.name}

        try:
            result = post(url, headers=headers, json=data)

            return result.content == b'{"code":0}'
        except:
            return 'ConnectionError'

    def Check_Password(self):
        url = 'https://www.shararam.ru/api/user/login'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Shararam/2.0.3 Chrome/80.0.3987.165 Electron/8.2.5 Safari/537.36'}

        data = {'login': self.name,
                'password': md5(self.password.encode()).hexdigest()}

        try:
            result = post(url, headers=headers, json=data)

            if result.content != b'{"code":0}':
                return False
            else:
                cookie = result.cookies.get_dict()
                Coockes(cookie['SessionId']).SaveCoockie()
        except:
            return 'ConnectionError'


class Coockes:
    def __init__(self, SessionId=''):
        self.SessionId = SessionId

        # Определяем путь к файлам куки
        path = abspath(__file__).split('\\')[:-2]
        self.path = '\\'.join(path + ['data', 'cookies.sqlite'])

    def SaveCoockie(self):
        print(self.path)

        # Подключаемся к файлу куки
        db = connect(self.path)

        # Изменяем значение SessionId
        db.execute('''UPDATE moz_cookies SET value = ? WHERE name = ?''',
                   (self.SessionId, 'SessionId'))

        # Сохраняем файл куки
        db.commit()

    def ClearCoockie(self):
        # Подключаемся к файлу куки
        db = connect(self.path)

        # Чистим SessionId
        db.execute('''UPDATE moz_cookies SET value = ? WHERE name = ?''',
                   ('', 'SessionId'))

        # Сохраняем файл куки
        db.commit()


r = Registration()
r.get_RandomUser()
r.Registration()

# a = Authorization('DDTE_30', '159753Qwe1')
# if a.Check_Name() == True:
#     a.Check_Password()
