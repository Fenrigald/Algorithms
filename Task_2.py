def count(numb, r, cnt):
    if numb < 1:
        return f'Количество четных цифр в числе - {cnt - r}, нечетных - {r})'
    elif (numb % 10) % 2 == 1:
        r += 1
        cnt += 1
        return count(numb // 10, r, cnt)
    cnt += 1
    return count(numb // 10, r, cnt)

numb = int(input('Введите число: '))
print(count(numb, 0, 0))