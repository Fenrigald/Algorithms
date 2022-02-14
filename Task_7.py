def formula(n):
    return 0 if n == 0 else n + formula(n - 1)


n = int(input('Введите кол-во натуральных чисел: '))
print(f'{int(n * (n + 1) / 2)} = {formula(n)}, формула верна')
