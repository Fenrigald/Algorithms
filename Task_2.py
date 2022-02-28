from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Время {mem_diff}")
        return res
    return wrapper


@memory
def my_func(n):
    def count_num(num, even=0, odd=0):
        if num == 0:
            return f'Количество четных и нечетных цифр: ({even}, {odd})'
        else:
            if num % 10 % 2 == 0:
                even += 1
            elif num % 10 % 2 == 1:
                odd += 1
            return count_num(num//10, even, odd)
    return n


my_func(12345678)


# "Завернул" функцию одну в другую, т.к. в рекурсии выводится слишком большое количество замеров