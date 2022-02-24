from collections import OrderedDict
from timeit import timeit


common_dict = {}
od_dict = OrderedDict()
print('Добавление элементов')
print(timeit("""for i in range(10):
                    common_dict[i]=i""", globals=globals(), number=100000))
print(timeit("""for i in range(10):
                    od_dict[i]=i""", globals=globals(), number=100000))
print('Чтение')
print(timeit("""for i in range(10):
                    common_dict[i]""", globals=globals(), number=100000))
print(timeit("""for i in range(10):
                    od_dict[i]""", globals=globals(), number=100000))
print('Сравнение словарей')
print(timeit('common_dict == common_dict', globals=globals(), number=100000))
print(timeit('od_dict == od_dict', globals=globals(), number=100000))

# Добавление элементов
# 0.058693300000000004
# 0.0793783
# Чтение
# 0.05081440000000001
# 0.06238929999999998
# Сравнение словарей
# 0.016295899999999974
# 0.02114480000000002
# Особой разницы между обычным и упорядоченным словарем не замечено.
# В версии 3.6 словари являются упорядоченными по-умолчанию.
# Стандартные словари в некотором роде удобнее, ведь не приходится думать о порядке.
# но в ситуациях, где порядок при сравнении критичен - необходим именно OrserDict
