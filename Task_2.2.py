from random import randint
from timeit import timeit


def without_sort(lst_obj):
    copy_lst = lst_obj[:]
    for i in range(len(lst_obj) // 2):
        copy_lst.remove(min(copy_lst))
    return min(copy_lst)


m = 10
orig_list_10 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина = {m}: '
      f'{timeit("without_sort(orig_list_10)", globals=globals(), number=1000)}')

m = 100
orig_list_100 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина = {m}: '
      f'{timeit("without_sort(orig_list_100)", globals=globals(), number=1000)}')

m = 1000
orig_list_1000 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина = {m}: '
      f'{timeit("without_sort(orig_list_1000)", globals=globals(), number=1000)}')


# Длина = 10: 0.0050373999999999974
# Длина = 100: 0.28997779999999995
# Длина = 1000: 31.521301100000002
