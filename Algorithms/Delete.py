from os.path import abspath
from os import walk, remove, system
from shutil import rmtree
from Algorithms.Shortcut import Shortcut

def Delete_All():
    # Получаем путь к папке проекта
    project = abspath(__file__).split('\\')[:-2]
    project = '\\'.join(project)

    # Удаляем все файлы проекта
    for path, dirnames, filenames in walk(project):
        for dir in dirnames:
            try:
                rmtree(path + '/' + dir)
            except:
                pass
        for file in filenames:
            try:
                remove(path + '/' + file)
            except:
                pass

    # Удаляем ярлык с рабочего стола
    shortcut = Shortcut()
    if shortcut.Check_System():
        if shortcut.Check_Shortcut():
            shortcut.Delete()

    # Открываем папку проекта, чтобы пользователь удалил то, что осталось
    system('explorer.exe ' + project)