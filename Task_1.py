import operator

def calculator():
    s = input('Введите знак операции(+,-,*,/). Для завершения введите 0: ' ).strip()
    oper = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    if s == '0':
        return
    else:
        try:
            n = int(input('Введите первое число: '))
            m = int(input('Введите второе число: '))
        except ValueError:
            print('Не строку. Число.')
            calculator()
        try:
            result = oper[s](n,m)
            print(result)
            return calculator()
        except ZeroDivisionError:
            print('На ноль делить можно... Но не в этом случае.')
            return calculator()

calculator()