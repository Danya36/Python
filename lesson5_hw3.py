"""Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open('homework5-3.txt', 'r') as my_file:
    last_name = []
    salary = []
    my_list = my_file.readlines().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           last_name.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {last_name}, средний оклад {sum(map(int, salary)) / len(salary)}')

# Выскакивает такая ошибка, не знаю как ее обойти:
# return codecs.charmap_decode(input,self.errors,decoding_table)[0]
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1: character maps to <undefined>