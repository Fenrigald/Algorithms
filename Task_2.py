from collections import defaultdict
from functools import reduce

"Первый вариант"


def insert_data(data):
    if type(data) == list:
        for item in data:
            num[item] = [item[n] for n in range(len(item))]
    else:
        num[data] = [data[n] for n in range(len(data))]


def convert(n):
    table = '0123456789ABCDEF'
    if n < 16:
        return table[n]
    x, y = divmod(n, 16)
    return convert(x) + table[y] if x else table[y]


def sum_hex(data):
    return convert(reduce(lambda a, b: int(a, 16) + int(b, 16), data))


def mul_hex(data):
    return convert(reduce(lambda a, b: int(a, 16) * int(b, 16), data))


def output(data, summ, mull):
    for key in data.keys():
        if key == summ:
            print(f'Сумма: {data[key]}')
        elif key == mull:
            print(f'Произведение: {data[key]}')
        else:
            print(f'Число {key} хранится как: {data[key]}')


"Второй вариант"


class Digits:

    def __init__(self):
        self.numbers = []

    def insert(self, *args):
        if len(self.numbers) == 0:
            data = input('Введите два числа: ').split(' ')
            for item in data:
                self.numbers.append([item[n] for n in range(len(item))])
        else:
            self.numbers.append([args[0][n] for n in range(len(args[0]))])

    def convert(self, *args):
        table = '0123456789ABCDEF'
        if args[0] < 16:
            return table[args[0]]
        x, y = divmod(args[0], 16)
        return self.convert(x) + table[y] if x else table[y]

    def __add__(self, other):
        num_one = num_two = ''
        for item in self.numbers[0]:
            num_one += item
        for item in other.numbers[1]:
            num_two += item
        return self.convert(int(num_one, 16) + int(num_two, 16))

    def __mul__(self, other):
        num_one = num_two = ''
        for item in self.numbers[0]:
            num_one += item
        for item in other.numbers[1]:
            num_two += item
        return self.convert(int(num_one, 16) * int(num_two, 16))

    def output(self):
        print(f'Первое число: {self.numbers[0]}')
        print(f'Второе число: {self.numbers[1]}')
        print(f'Результат первой операции: {self.numbers[2]}')
        print(f'Результат второй операции: {self.numbers[3]}')


if __name__ == '__main__':

    num = defaultdict(list)
    user_data = input('Введите два числа: ').split(' ')

    insert_data(user_data)
    rez_sum = sum_hex(num)
    rez_mul = mul_hex(num)
    insert_data(rez_sum)
    insert_data(rez_mul)
    output(num, rez_sum, rez_mul)

    two_numbers = Digits()
    two_numbers.insert()
    two_numbers.insert(two_numbers + two_numbers)
    two_numbers.insert(two_numbers * two_numbers)
    two_numbers.output()