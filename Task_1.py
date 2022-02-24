from collections import namedtuple
from statistics import mean

def count_sum(count_company=int(input('Кол-во компаний: '))):
    company = namedtuple('company', 'name first second third four total')
    company_list = []
    avg = []
    up_avg = []
    down_avg = []
    for i in range(count_company):
        name = input('Название компании: ')
        profit = [int(i) for i in input(
            'Прибыль компании '
            'за каждый квартал (введите через пробле каждый квартал. Всего 4 квартала): ').split(' ')]
        try:
            new = company(
                name=name,
                first=profit[0],
                second=profit[1],
                third=profit[2],
                four=profit[3],
                total=sum(profit)
            )
        except IndexError:
            return f'Прибыль указана неверно'
        company_list.append(new)
        avg.append(sum(profit))
    for i in range(len(company_list)):
        if company_list[i].total > mean(avg):
            up_avg.append(company_list[i].name)
        else:
            down_avg.append(company_list[i].name)
    return f'Предприятия, с прибылью выше среднего значения: {up_avg}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {down_avg}'


if __name__ == '__main__':
    print(count_sum())