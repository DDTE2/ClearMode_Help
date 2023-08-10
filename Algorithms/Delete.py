from os.path import abspath
from os import walk, remove, system
from shutil import rmtree

def Delete_All():
    # Получаем путь к папке проекта
    project = abspath(__file__).split('\\')[:-2]
    project = '\\'.join(project)

    # Удаляем всё
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

    # Открываем папку проекта, чтобы пользователь удалил то, что осталось
    system('explorer.exe ' + project)