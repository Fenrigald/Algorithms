def seq(n, r):
    return 0 if n == 0 else r + seq(n-1, - r / 2)

n = int(input('Введите кол-во элементов: '))
print(f'Кол-во элементов - {n}, сумма - {seq(n, 1)}')