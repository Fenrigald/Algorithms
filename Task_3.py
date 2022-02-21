from timeit import timeit
from random import randint


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(digit):
    return str(digit) if digit // 10 == 0 else str(digit - (digit // 10) * 10) + str(revers_4(digit // 10))


if __name__ == "__main__":
    number = randint(10000, 1000000)

    print(timeit("revers(number)", globals=globals(), number=10000))
    print(timeit("revers_2(number)", globals=globals(), number=10000))
    print(timeit("revers_3(number)", globals=globals(), number=10000))
    print(timeit("revers_4(number)", globals=globals(), number=10000))


# 0.013839300000000002
# 0.009120499999999997
# 0.0028943999999999984
# 0.026752799999999993

# Третий вариант самый быстрый.
# - В этом варианте не происходит вычислений, а преобразование проводится стандартной функцией;
