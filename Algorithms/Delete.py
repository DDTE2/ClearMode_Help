from os.path import abspath
from os import walk, remove
from shutil import rmtree

prpject = abspath(__file__).split('\\')[:-2]
prpject = '\\'.join(prpject)

for path, dirnames, filenames in walk(prpject):
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