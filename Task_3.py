def revers_ch(n):
    return '' if n == 0 else f'{str(n % 10)}{revers_ch(n // 10)}'


n = input('Введите число: ')
if n[0] == '0':
    print(f'{revers_ch(int(n))}0')
else:
    print(revers_ch(int(n)))
