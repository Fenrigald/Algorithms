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
def revers(enter_num):
    x = [str(a) for a in str(enter_num)]
    x.reverse()
    return ''.join(x)


@memory
def revers_2(enter_num):
    x = map(int, str(enter_num))
    x_1 = list(map(str, x))
    x_1.reverse()
    return ''.join(x_1)


revers(12345679)
revers_2(12345679)


# До оптимизации 0.01171875
# После оптимизации 0.0 Mib
# Заменил генератор на map