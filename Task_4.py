from timeit import timeit
from random import randint


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Самое частое число {num}. Появлялось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Самое частое число {elem}. Появлялось в массиве {max_2} раз(а)'


def func_3():
    max_el = max([(x, array.count(x)) for x in set(array)], key=lambda x: x[1])
    return f'Самое частое число {max_el[0]}. Появлялось в массиве {max_el[1]} раз(а)'

array = [randint(1, 10) for i in range(1000)]
print(f'{func_1()}, время выполнения: {timeit("func_1()", globals=globals(), number=1000):.7f}')
print(f'{func_2()}, время выполнения: {timeit("func_2()", globals=globals(), number=1000):.7f}')
print(f'{func_3()}, время выполнения: {timeit("func_3()", globals=globals(), number=1000):.7f}')

# Самое частое число 10. Появлялось в массиве 120 раз(а), время выполнения: 10.3059426
# Самое частое число 10. Появлялось в массиве 120 раз(а), время выполнения: 10.1592131
# Самое частое число 10. Появлялось в массиве 120 раз(а), время выполнения: 0.1104938


# Реализовал перебор не по всем элементам, а лишь по уникальным.
# За счет этого сумел добиться оптимизации времени работы.
# Чем больше повторяющихся элементов в списке, тем эффективнее приведенный алгоритм