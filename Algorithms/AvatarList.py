from os.path import abspath
from os import walk

class Avatars:
    def __init__(self):
        # Номера доступных и недоступных образов
        self.public = self.secret = 0

        # Назначаем путь к изображениям аватаров
        path = abspath(__file__).split('\\')[:-2]
        self.path = '\\'.join(path + ['GUI', 'Avatars'])

        self.PublicAvatar = self.get_AvatarList('Public')
        self.SecretAvatar = self.get_AvatarList('Secret')

    def get_AvatarList(self, type):
        for path, dirnames, filenames in walk(f'{self.path}/{type}/'):
            avatarsID = sorted({int(i[:-4]) for i in filenames})

        Avatars = {}
        for i in range(len(avatarsID)):
            Avatars[i] = {'id': avatarsID[i],
                          'image': f'{self.path}\\{type}\\{avatarsID[i]}.png'}

        return Avatars

    def get_PublicAvatar(self, increment=1):
        self.public = (self.public + increment) % len(self.PublicAvatar)

        return self.PublicAvatar[self.public]

    def get_SecretAvatar(self, increment=1):
        self.secret = (self.secret + increment) % len(self.SecretAvatar)

        return self.SecretAvatar[self.secret]