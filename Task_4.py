from hashlib import sha512
from uuid import  uuid4

class Main():
    def __init__(self):
        self.hash = {}
        self.salt = 'salt'


    def get_hash(self, url):
        salt = uuid4().hex
        print(f'Соль: {salt}')
        hash_url = sha512(salt.encode() + url.encode()).hexdigest()
        return hash_url


    def check_url(self,url):
        new = self.get_hash(url)
        if url not in self.hash.keys():
            self.hash[url] = new
            print(f'Url {url} добавлен в хеш')
            print('-' * 50)
        else:
            print(f'В хеше уже есть url {url}')
            print(f'Хеш url-a: {self.hash[url]}')
            print('-' * 50)

    def print_hash(self):
        print(self.hash)

m = Main()
m.check_url('www.vk.ru')
m.check_url('www.vk.ru')
m.check_url('www.notvk.ru')
m.check_url('www.notvk.ru')
m.print_hash()