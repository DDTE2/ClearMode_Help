# GUI
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import qdarktheme
from GUI.Scripts.main_window import Ui_ClearMod_Window
import sys
# Данные о ПК
from Algorithms.SystemData import System
from os.path import abspath
# Формат данных
from json import dumps, loads
# Работа с файлами
from os import walk
# Мои модули
from Algorithms.AvatarList import Avatars
from Algorithms.LogIn import *


class Window(QtWidgets.QMainWindow, Ui_ClearMod_Window):
    def __init__(self):
        # Наследуем классы интерфейса
        QtWidgets.QMainWindow.__init__(self)
        super(Ui_ClearMod_Window).__init__()

        # Получаем директорию проекта
        path = abspath(__file__).split('\\')[:-1]
        self.path = '\\'.join(path)

        # Загружаем пользовательские настройки
        self.LoadSettings()

        # Настриваем интерфейс
        self.setupUi(self)
        self.Load_run_settings()  # Настраиваем окно запуска лаунчера
        self.SystemData()  # Выводим на экран системную информацию
        self.setIcon()  # Устанавливаем изображения
        self.Registration()  # Настраиваем окно регистрации
        self.Authorization()  # Настраиваем окно авторизации
        self.Add_UsersList()  # Добавляем список пользователей в окно авторизации

    def SystemData(self):  # Отображаем системную информацию
        data = System()  # Получаем информацию о ПК

        # Выводим на экран системную информацию
        if self.ShowSystemData_checkBox.isChecked():
            self.OSname_label.setText('-')
            self.MACadress_label.setText('-')
            self.IParress_label.setText('-')
        else:
            system = data.system
            self.OSname_label.setText(system['system'])
            self.MACadress_label.setText(system['mac-adress'])
            self.IParress_label.setText(system['ip-adress'])

        self.ShowSystemData_checkBox.clicked.connect(self.SystemData)

        # Выводим на экран список установленых лаунчеров
        launchers = data.launchers
        if launchers['Shararam']:
            self.Shararam_Value_label.setText('Усановлен')
        else:
            self.Shararam_Value_label.setText('Не усановлен')
        if launchers['private']:
            self.Private_value_label.setText(launchers['private'])
        else:
            self.Private_value_label.setText('Не установлены')

        # Выводим на экран список установленых программ
        software = data.software
        if software['WPE PRO']:
            self.WPE_value_label.setText('Запущен')
        else:
            self.WPE_value_label.setText('Не запущен')
        if software['Wireshark']:
            self.Wireshark_value_label.setText('Запущен')
        else:
            self.Wireshark_value_label.setText('Не запущен')
        if software['Charles Proxy']:
            self.Charles_value_label.setText('Запущен')
        else:
            self.Charles_value_label.setText('Не запущен')
        if software['Fiddler']:
            self.Fiddler_value_label.setText('Запущен')
        else:
            self.Fiddler_value_label.setText('Не запущен')
        if software['VPN']:
            self.VPN_value_label.setText('Запущен')
        else:
            self.VPN_value_label.setText('Не запущен')

    def Load_run_settings(self):  # Загружаем настройки запуска пользователя
        # Настраиваем тему
        if self.settings['run']['theam'] == 'dark':
            self.DarkTheam_radioButton.setChecked(True)
        else:
            self.LighTheam_radioButton.setChecked(True)
        # Настраиваем перезагрузку
        if self.settings['run']['reboot']:
            self.reboot_checkBox.setChecked(True)
        else:
            self.reboot_checkBox.setChecked(False)

        self.Start_button.clicked.connect(self.ClearMode_RunMenu)

    def ClearMode_RunMenu(self):  # Меню запуска Clear Mod
        # Сораняем настройки
        if self.LighTheam_radioButton.isChecked():
            self.settings['run'] = {'theam': 'light'}
        else:
            self.settings['run'] = {'theam': 'dark'}

        self.settings['run']['reboot'] = self.reboot_checkBox.isChecked()
        self.SaveSattings()

    def Registration(self):  # Меню регистрации
        # Назначаем функцию на кнопку показа паороля
        self.ShowPassword_checkBox.clicked.connect(self.ShowPassword)
        # Настраиваем кнопки выбора аватара
        self.LeftPublicAvatar_button.clicked.connect(self.LeftPublicAvatar_choiser)
        self.RightPublicAvatar_button.clicked.connect(self.RightPublicAvatar_choiser)
        self.LeftSecretAvatar_button.clicked.connect(self.LeftSecretAvatar_choiser)
        self.RightSecretAvatar_button.clicked.connect(self.RightSecretAvatar_choiser)

        # Генерация случайных данных
        self.UserGen_button.clicked.connect(self.RandUser_gen)
        # Проверка данных
        self.CheckData_button.clicked.connect(self.Check_RegData)
        # Регистрация аккаунта
        self.Reg_button.clicked.connect(self.Reg)

    def Authorization(self):  # Меню авторизации
        self.ShowPassword2_checkBox.clicked.connect(self.ShowPassword2)
        self.UsersList_comboBox.activated.connect(self.Account_Choise)
        self.Login_Button.clicked.connect(self.LogIn)

    def ShowPassword(self):  # Кнопка показа пароля в меню регистрации
        if self.ShowPassword_checkBox.isChecked():
            self.Password_input.setEchoMode(0)
        else:
            self.Password_input.setEchoMode(2)

    def ShowPassword2(self):  # Кнопка показа пароля в меню авторизации
        if self.ShowPassword2_checkBox.isChecked():
            self.Password_input_2.setEchoMode(0)
        else:
            self.Password_input_2.setEchoMode(2)

    def LoadSettings(self):  # Загружаем настройки пользователя
        try:
            with open(self.path + '/data/settings.json', 'r') as file:
                self.settings = loads(file.read())

        except:
            self.settings = {'run': {'theam': 'light', 'reboot': False}}

    def SaveSattings(self):  # Сохраняем настройки пользователя
        with open(self.path + '/data/settings.json', 'w') as file:
            file.write(dumps(self.settings, indent=4))

    def closeEvent(self, *args, **kwargs):  # Скрипты, выполняемые, после закрытия основного окна
        super(QtWidgets.QMainWindow, self).closeEvent(*args, **kwargs)

        # Созраняем данные
        self.SaveSattings()

    def setIcon(self):  # Назначеам изображения
        # Устанавливаем иконку мода
        ico = self.path + '/GUI/Icons/ClearMod.ico'
        self.setWindowIcon(QtGui.QIcon(ico))

        # Добавляем переменную, хранящую возможные аватары пользователей
        self.avatars = Avatars()
        # Добавляем в меню регистрации общедоступный образ
        PublicAvatar = QtGui.QPixmap(self.path + '/GUI/Avatars/Public/2.png')
        self.PublicAvatar_image.setPixmap(PublicAvatar)
        self.PublicAvatar_image.setAlignment(Qt.AlignCenter)
        # Добавляем в меню регистрации недоступный образ
        SecretAvatar = QtGui.QPixmap(self.path + '/GUI/Avatars/Secret/0.png')
        self.SecretAvatar_image.setPixmap(SecretAvatar)
        self.SecretAvatar_image.setAlignment(Qt.AlignCenter)

    def LeftPublicAvatar_choiser(self):  # Функция выбора общедоступного аватара
        avatar = self.avatars.get_PublicAvatar(-1)

        PublicAvatar = QtGui.QPixmap(avatar['image'])
        self.PublicAvatar_image.clear()
        self.PublicAvatar_image.setPixmap(PublicAvatar)
        self.PublicAvatar_image.setAlignment(Qt.AlignCenter)

    def RightPublicAvatar_choiser(self):  # Вторая функция выбора общедоступного аватара
        avatar = self.avatars.get_PublicAvatar()

        PublicAvatar = QtGui.QPixmap(avatar['image'])
        self.PublicAvatar_image.clear()
        self.PublicAvatar_image.setPixmap(PublicAvatar)
        self.PublicAvatar_image.setAlignment(Qt.AlignCenter)

    def LeftSecretAvatar_choiser(self):  # Функция выбора недоступного аватара
        avatar = self.avatars.get_SecretAvatar(-1)

        SecretAvatar = QtGui.QPixmap(avatar['image'])
        self.SecretAvatar_image.clear()
        self.SecretAvatar_image.setPixmap(SecretAvatar)
        self.SecretAvatar_image.setAlignment(Qt.AlignCenter)

    def RightSecretAvatar_choiser(self):  # Вторая функция выбора недоступного аватара
        avatar = self.avatars.get_SecretAvatar()

        SecretAvatar = QtGui.QPixmap(avatar['image'])
        self.SecretAvatar_image.clear()
        self.SecretAvatar_image.setPixmap(SecretAvatar)
        self.SecretAvatar_image.setAlignment(Qt.AlignCenter)

    def RandUser_gen(self):  # Функция генерации случайных данных
        user = Registration()
        user.get_RandomUser()

        self.Login_input.setText(user.name)
        if len(self.Password_input.text()) < 4:
            self.Password_input.setText(user.password)

    def Check_RegData(self):  # Функция проверки данных для регистрации
        # Копируем логин и пароль
        name = self.Login_input.text()
        password = self.Password_input.text()

        # Проверяем логин и пароль
        self.Message_label.setStyleSheet('color: red')
        match Check_Data(name, password):
            case 'NameLen_Error':
                self.Message_label.setText('Имя смешарика должно быть длинее 3-х символов!')
            case True:
                self.Message_label.setText('Это имя уже занято!')
            case 'PasswordLen_Error':
                self.Message_label.setText('Пароль смешарика должно быть длинее 3-х символов!')
            case 'ConnectionError':
                self.Message_label.setText('Возникли проблемы при подключении к серверу.')
            case 'NameText_Error':
                self.Message_label.setText('Недопустимое имя смешарика!')
            case 'NameSymbol_Error':
                self.Message_label.setText('Имя смешарика может содержать только буквы и цифры!')
            case _:
                self.Message_label.setStyleSheet('color: lightblue')
                self.Message_label.setText('Вы можете создать смешарика.')

                return True
        return False

    def Reg(self):  # Регистрация аккаунта
        # Проверяем данные на корректность
        if not self.Check_RegData():
            return None

        # Определяем выбранный пользователем аватар
        if self.Avatar_widget.currentIndex():
            avatar = self.avatars.SecretAvatar[self.avatars.secret]['id']
        else:
            avatar = self.avatars.PublicAvatar[self.avatars.public]['id']

        # Регистрируем пользователя
        data = Registration(name=self.Login_input.text(),
                            password=self.Password_input.text(),
                            avartar=avatar,
                            referal=self.Referal_input.text())

        try:
            sessionId = data.Registration()
            # Уведомляем пользователя
            if sessionId:
                self.Message_label.setStyleSheet('color: lightblue')
                self.Message_label.setText('Смешарик успешно создан!')

                self.Add_UsersList()
            else:
                self.Message_label.setStyleSheet('color: red')
                self.Message_label.setText('Произошла неизвестная ошибка!')
        except:
            self.Message_label.setStyleSheet('color: red')
            self.Message_label.setText('Произошла неизвестная ошибка!')

    def Add_UsersList(self):  # Создаём список аккаунтов
        self.UsersList_comboBox.clear()
        with open(self.path + '/data/users.json', 'r') as file:
            data = loads(file.read())
        for i in data:
            self.UsersList_comboBox.addItem(i['Имя'])

        self.Account_Choise()

    def Account_Choise(self):  # Функция выбора аккаунта при авторизации
        userId = self.UsersList_comboBox.currentIndex()

        with open(self.path + '/data/users.json', 'r') as file:
            users = loads(file.read())

            data = users[userId]
            self.Login_input_2.setText(data['Имя'])
            self.Password_input_2.setText(data['Пароль'])

    def LogIn(self):  # Авторизация в игре
        # Меняем цвет увидомления на красный
        self.LoginError_label.setStyleSheet('color: red')

        # Считываем введённые пользователем логин и пароль
        name = self.Login_input_2.text()
        password = self.Password_input_2.text()

        # Осуществляем авторизацию
        LoginResult = Authorization(name, password)

        # Выводим ошибку на экран
        match LoginResult:
            case 'NameLen_Error':
                self.LoginError_label.setText('Имя должно быть длинее 3-х символов!')
                return False
            case 'PasswordLen_Error':
                self.LoginError_label.setText('Пароль должен быть длинее 3-х символов!')
                return False
            case 'ConnectionError':
                self.LoginError_label.setText('Возникли проблемы при подключении к серверу.')
                return False
            case 'NameText_Error':
                self.LoginError_label.setText('Недопустимое имя смешарика!')
                return False
            case 'NameSymbol_Error':
                self.LoginError_label.setText('Имя может содержать только буквы и цифры!')
                return False
            case 'WromgPassword_Error':
                self.LoginError_label.setText('Неверный пароль!')
                return False
            case False:
                self.LoginError_label.setText('При подключении к серверу произошла ошибка!')
                return False

        # Добавляем аккаунт в список пользователей
        Save_User().add_user(name=self.Login_input_2.text(),
                             password=self.Password_input_2.text())
        self.Add_UsersList()

        # Уведомляем пользователя об успешной регистрации
        self.LoginError_label.setStyleSheet('color: lightblue')
        self.LoginError_label.setText('Вход в игру прошёл успешно.')


app = QApplication(sys.argv)
qdarktheme.setup_theme()
application = Window()
application.show()

sys.exit(app.exec())
