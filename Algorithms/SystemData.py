from uuid import getnode  # MAC-адрес
from platform import system, release  # Версия системы
from json import dumps  # Форматирование данных
from requests import get  # GET-запросы
# Работа с папками
from os.path import exists
from os import getenv
from psutil import process_iter  # Список процессов


class System:
    def __init__(self):
        self.system = self.Get_SystemData()
        self.launchers = self.Get_launchers()
        self.software = self.Get_Software()

    def __str__(self):
        return dumps(self.__dict__, ensure_ascii=False, indent=4)

    def Get_SystemData(self):
        # Операционная система
        data = {'system': system() + ' ' + release()}

        # MAC-адрес
        mac = hex(getnode())[2:]
        data['mac-adress'] = ':'.join([mac[i:i + 2] for i, j in enumerate(mac) if not (i % 2)])

        # IP-адрес
        try:
            data['ip-adress'] = get('https://api.ipify.org').content.decode('utf8')
        except:
            data['ip-adress'] = 'Сервис недоступен.'

        return data

    def Get_launchers(self):
        data = {'Clear Mode': True}

        # Проверяем, установлен ли официальный лаунчер шарарама
        AppData_path = getenv('LOCALAPPDATA') + '/Programs/'
        data['Shararam'] = exists(AppData_path + 'Shararam')

        # Проверяем, установлены ли приватки
        data['private'] = []
        if exists(AppData_path + 'sxlauncher'):
            data['private'].append('SxDale')
        if exists(AppData_path + 'MDLauncher'):
            data['private'].append('MiDale')

        return data

    def Get_Software(self):
        data = {i: False for i in ('WPE PRO', 'Wireshark', 'Charles Proxy', 'Fiddler', 'VPN')}

        for proces in process_iter():
            name = proces.name().lower()[:-4]
            match name:
                case 'charles':
                    data['Charles Proxy'] = True
                case 'wpe pro':
                    data['WPE PRO'] = True
                case 'wpe pro 0 delay':
                    data['WPE PRO'] = True
                case 'fiddler':
                    data['Fiddler'] = True
                case "wireshark":
                    data['Wireshark'] = True
                case _:
                    if 'vpn' in name:
                        data['VPN'] = True

        return data