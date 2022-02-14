from random import randint

def attem(n, attempt):
    if attempt == 0:
        return f'Вы проиграли, загаданное число: {n}'
    r = int(input('Угадайте число от 0 до 100: '))
    if r == n:
        return f'Верно, загаданное число: {n}'
    elif n > r:
        print(f'Загадонное число больше предложенного, осталось {attempt} попыток')
        return attem(n, attempt - 1)
    else:
        print(f'Загадонное число меньше предложенного, осталось {attempt} попыток')
        return attem(n, attempt - 1)

n = randint(0, 100)
print(attem(n, 9))