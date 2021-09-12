"""Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл."""

import json

with open('homework5-7.txt', 'r', encoding='cp1251') as file:
    for elem in file:
        print(elem)

profit = {}
pr = {}
prof = 0
average_profit = 0
i = 0
with open('homework5-7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split(' ')
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Average profit - {average_profit}')
    else:
        print(f'Loss')
    pr = {'Average profit': round(average_profit)}
    profit.update(pr)
    print(f'Profit of each company:  {profit}')

with open('homework5-7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Created file json:  \n '
          f' {js_str}')