# ~
import time

def dec(func):
    def wrp(values):
        a = time.time()
        r = func(values)
        b = time.time()
        print(f'время исполнения: {b - a} секунд')
        return r
    return wrp


def dec2(func):
    def wrp():
        a = time.time()
        func()
        b = time.time()
        print(f'время исполнения: {b - a} секунд')
    return wrp


quantity = 100000
val = [i for i in range(quantity)]
val2 = val.copy()
index_or_keys = [i for i in range(1, quantity, 20)]


# A

@dec
def dict(val):
    '''O(1)'''
    d = {}
    for num, val in enumerate(val):  # O(N)
        d[num] = val  # O(1)
    print('Заполняем словарь: ', end='')
    return d


@dec
def list(val):
    '''O(N)'''
    l = []
    for val in val:  # O(N)
        l.append(val)  # O(1)
    print('Заполняем список: ', end='')
    return l

print('A','-' * 50)
d = dict(val2)
l = list(val)
'''
Заполняем словарь: время исполнения: 0.010993003845214844 секунд
Заполняем список: время исполнения: 0.005005359649658203 секунд
Словарь заполняется в два раза медленнее, чем список. Алгоритм недопущения коллизий, 
срабатывающий при создании нового элемента в словаре, тратит время
'''

# B

@dec
def gt_fr_di(keys):
    '''O(1)'''
    print(f'Берем из словаря по ключу: ', end='')
    for i in keys:
        r = d[i]


@dec
def gt_fr_li(indexes):
    '''O(N)'''
    print(f'Берем из списка по индексу: ', end='')
    for i in indexes:
        r = l[i]


print('B','-' * 50)
gt_fr_di(index_or_keys)
gt_fr_li(index_or_keys)

'''
Берем из словаря по ключу: время исполнения: 0.00099945068359375 секунд
Берем из списка по индексу: время исполнения: 0.0009989738464355469 секунд
Получение элемента из списка по индексу проходит в 2 раза быстрее, чем из словаря
'''


# C

@dec2
def dl_fr_li():
    '''O(1)'''
    print(f'Удаляем из списка по индексу: ', end='')
    del l[20]


@dec2
def dl_fr_di():
    '''O(1)'''
    print(f'Удаляем из словаря по ключу: ', end='')
    del d[20]


print('C','-' * 50)
dl_fr_li()
dl_fr_di()

# del_from_di(index_or_keys)

'''
Удаляем из списка по индексу: время исполнения: 0.0009996891021728516 секунд
Удаляем из словаря по ключу: время исполнения: 0.0 секунд (слишком быстрая операция, малое значение времени
автоматически округляется)
Удаление из словаря по ключу проходит заметно быстрее, чем удаление из списка по индексу, 
ведь при удалении из списка происходит его полное перестроение с перестановкой индексов
'''