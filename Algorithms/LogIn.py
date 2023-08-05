from random import choice, randint
from json import dumps, loads
from sqlite3 import connect
from requests import post
from os.path import abspath
from hashlib import md5
from datetime import datetime


class Registration:  # Класс регистрации в игре
    def __init__(self, name='', password='', referal='', avartar=0):
        # Получакм на вход данные пользователя
        self.name = name
        self.password = password
        self.referal = referal
        self.avartar = avartar

    def get_RandomUser(self):  # Функция создания случайных данных пользователя
        # Случайное имя
        self.name = self.RandomStr_gen(symbols='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                       lenght=randint(4, 12))
        # Случайный парроль
        self.password = self.RandomStr_gen(
            symbols='!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё',
            lenght=12)

    def RandomStr_gen(self, symbols='', lenght=4):  # Функция генерации случайной строки
        res = ''

        while lenght:
            res += choice(symbols)
            lenght -= 1

        return res

    def __str__(self):
        return dumps(self.__dict__, ensure_ascii=False)

    def Registration(self):  # Функция регистрации в игре
        url = 'https://www.shararam.ru/async/Register'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Shararam/2.0.3 Chrome/80.0.3987.165 Electron/8.2.5 Safari/537.36'}

        data = {'login': self.name,
                'password': self.password,
                'avatarid': self.avartar,
                'email': '',
                'referalName': self.referal}

        # Отправляем запрос
        result = post(url, headers=headers, json=data)
        cookie = result.cookies.get_dict()

        # Сохраняем ID сессии из куки
        SessionId = cookie['SessionId']
        Coockes(SessionId).SaveCoockie()

        return SessionId


class Authorization:
    def __init__(self, name='', password=''):
        self.name = name
        self.password = password

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


def Check_Data(name='', password=''):
    # Проверяем длину данных
    if len(name) < 4:
        return 'NameLen_Error'
    elif len(password) < 4:
        return 'PasswordLen_Error'

    # Проверяем ник на существование
    url = 'https://www.shararam.ru/api/user/check_login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Shararam/2.0.3 Chrome/80.0.3987.165 Electron/8.2.5 Safari/537.36'}

    data = {'login': name}

    try:
        result = post(url, headers=headers, json=data)
        if result.content == b'{"code":0}':
            return True
        else:
            # Проверяем ник на корректность
            url = 'https://www.shararam.ru/async/RegisterValidate'
            data = {'code': 0,
                    'data': name}

            result = post(url, headers=headers, json=data)
            match loads(result.content.decode())['errorCode']:
                case 0:
                    return False
                case -6:
                    return 'NameText_Error'
                case -3:
                    return 'NameSymbol_Error'
                case _:
                    print(loads(result.content.decode())['errorCode'])
                    return False
    except:
        return 'ConnectionError'


class Coockes:
    def __init__(self, SessionId=''):
        self.SessionId = SessionId

        # Определяем путь к файлам куки
        path = abspath(__file__).split('\\')[:-2]
        self.path = '\\'.join(path + ['data', 'cookies.sqlite'])

    def SaveCoockie(self):
        print(int(datetime.today().timestamp()) * 2)
        # Подключаемся к файлу куки
        db = connect(self.path)

        # Изменяем значение SessionId
        date = int(datetime.today().timestamp())
        creation = date * 10 ** 6
        db.execute(
            '''UPDATE moz_cookies SET value = ?, expiry = ?, lastAccessed = ?, creationTime = ? WHERE name = ?''',
            (self.SessionId,
             date * 2,
             creation,
             creation,
             'SessionId'))

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


class Save_User:
    def __init__(self):
        # Определяем путь к файлу с данными пользователя
        path = abspath(__file__).split('\\')[:-2]
        self.path = '\\'.join(path + ['data', 'users.json'])

        # Читаем данные
        self.read_data()

    def read_data(self):  # Читаем данные
        try:
            with open(self.path, 'r') as file:
                self.users = loads(file.read())
        except:
            self.users = []

    def add_user(self, name='', password=''):  # Добавляем данные
        # Проверяем, если ли аккунт в списке и изменяем/добавляем его
        i = 0
        flag = False
        while i < len(self.users):
            user = self.users[i]
            if user['Имя'] == name:
                self.users[i] = {'Имя': name, 'Пароль': password}
                flag = True
            i += 1
        if not flag:
            self.users.append({'Имя': name, 'Пароль': password})

        with open(self.path, 'w') as file:
            file.write(dumps(self.users, ensure_ascii=False, indent=4))
