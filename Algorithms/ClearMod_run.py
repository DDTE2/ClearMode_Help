from os import getenv, walk, system, remove
from os.path import abspath, exists
from shutil import rmtree, move
from zipfile import ZipFile
import subprocess
from psutil import process_iter


class ClearMod:
    def __init__(self, theam='light', reboot=False):
        if reboot:
            self.ClearAppdata()  # Чистим %appdata%
            # Перезагружаем компьютер
            try:
                system('shutdown -t 0 -r -f')
            except Exception as error:
                print(error)
        else:
            path = abspath(__file__).split('\\')[:-2]
            self.path = '\\'.join(path + ['Clear Mod'])

            self.theam = theam

    def ClearAppdata(self):
        appdata = getenv('APPDATA')

        for path, dirnames, filenames in walk(appdata):
            dir = path.split('\\')[-1].lower()
            if dir in ('adobe', 'mozilla', 'macromedia', 'shararam'):
                try:
                    rmtree(path)
                except:
                    pass

    def Run(self):
        # Удаляем не удалённые папки
        if exists(self.path + '/cache'):
            rmtree(self.path + '/cache')
        if exists(self.path + '/mode'):
            rmtree(self.path + '/mode')

        # Разархивируем файлы мода
        with ZipFile(self.path + '/skeleton.zip', 'r') as file:
            file.extractall(self.path + '/mode')

        with ZipFile(self.path + '/mode.zip', 'r') as file:
            file.extractall(self.path + '/cache')

        # Заменяем файлы, в зависимости от темы
        match self.theam:
            case 'light':
                move(self.path + '/cache/whitecache/Cache', self.path + '/mode/Profiles/knszpk5o.default')
                move(self.path + '/cache/whiteadblock/adblockplus', self.path + '/mode/Profiles/knszpk5o.default')
            case 'dark':
                move(self.path + '/cache/blackcache/Cache', self.path + '/mode/Profiles/knszpk5o.default')
                move(self.path + '/cache/blackadblock/adblockplus', self.path + '/mode/Profiles/knszpk5o.default')

        # Удаляем лишнее
        try:
            rmtree(self.path + '/cache')
        except Exception as error:
            print(error)

        # Импортируем файл куки
        coockies = self.path.split('\\')[:-1]
        coockies = '\\'.join(coockies + ['data', 'cookies.sqlite'])
        with open(coockies, 'rb') as file:
            data = file.read()
        with open(self.path + '/mode/Profiles/knszpk5o.default/cookies.sqlite', 'wb') as file:
            file.write(data)

        try:
            subprocess.call(self.path + '/mode/km.exe')
        except Exception as error:
            print(error)

    def Delete(self):  # Удаляем лишние папки и файлы
        for path, dirnames, filenames in walk(self.path):
            print(dirnames)
            for file in filenames:
                if not (file in {'mode.zip', 'skeleton.zip'}):
                    try:
                        remove(self.path + '/' + file)
                    except:
                        pass
            for dir in dirnames:
                try:
                    rmtree(path + '/' + dir)
                except Exception as error:
                    print(error)

    def Close(self):  # Функция завершения работы мода
        # Завершаем процесс
        proc = self.isStarted()
        if proc:
            proc.terminate()

        self.Delete()  # Удаляем лишние файлы

    def isStarted(self):
        for proc in process_iter():
            if proc.name() == 'km.exe':
                return proc
        return False

