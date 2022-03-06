from random import randint
from timeit import timeit


def gnome_sort(lst_obj):
    i = 1
    while i < len(lst_obj):
        if not i or lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
            i -= 1
    return lst_obj[m]


m = 10
orig_list_10 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина {m}: '
      f'{timeit("gnome_sort(orig_list_10[:])", globals=globals(), number=100)}')

m = 100
orig_list_100 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина {m}: '
      f'{timeit("gnome_sort(orig_list_100[:])", globals=globals(), number=100)}')

m = 1000
orig_list_1000 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Длина {m}: '
      f'{timeit("gnome_sort(orig_list_1000[:])", globals=globals(), number=100)}')


# Длина 10: 0.0031868
# Длина 100: 0.3797821
# Длина 1000: 54.7335455
