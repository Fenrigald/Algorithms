from timeit import timeit

my_list = [i for i in range(1000)]


# Изначальный вариант
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Другой вариант
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# Сравнение времени
def func_time_compare(func_1, func_2):
    res_1 = timeit("func_1(my_list)", globals=globals(), number=1)
    print(res_1)
    res_2 = timeit("func_2(my_list)", globals=globals(), number=1)
    print(res_2)
    return ((res_1 - res_2) / res_1) * 100


print(f'Разница вов ремени: {func_time_compare(func_1, func_2):.2f} %')

#
# Удалось снизить время выполнения примерно на 20% (Значения разницы скачут от 9 и вплоть до 40 процентов).
# Во втором варианте решения применил list comprehension.
# 8.009999999999962e-05
# 6.260000000000293e-05
# Разница во времени: 21.85%
