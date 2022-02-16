from hashlib import pbkdf2_hmac
from binascii import hexlify
import sqlite3


def get_hash_pwd():
    p = input('Введите пароль: ')
    p = bytes(p.encode('utf-8'))
    slt = b'salt'
    p = pbkdf2_hmac(hash_name='sha256', password = p, salt=slt, iterations=10000)
    p = hexlify(p)
    return p


def save_in_db(p):
    login = 'test_login'
    cursor.execute(f'CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, login text not null, password text);')
    item = (1,login,p)
    cursor.execute(f"INSERT INTO users VALUES(*, *, *);", item)
    conn.commit()


def get_from_db():
    cursor.execute("SELECT * FROM users")
    res = cursor.fetchone()
    h = res[2]
    print(f'Строка в базе данных: {h}')
    conn.close()
    return h


conn = sqlite3.connect(":memory:")  # ('exampleDB.db')
cursor = conn.cursor()
p = get_hash_pwd()
save_in_db(p)
db_h = get_from_db()
new_h = get_hash_pwd()
if db_h == new_h:
    print(f'Пароли совпадают')
else:
    print('Пароли отличаются')