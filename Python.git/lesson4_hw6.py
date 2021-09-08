'''Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.'''

#a
from itertools import count

def my_count_func(first_number, last_number):
    for el in count(first_number):
        if el > last_number:
            break
        else:
            print(el)

#b
from itertools import cycle

def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1

my_count_func(first_number = int(input("Enter first number: ")), last_number = int(input("Enter last number: ")))
my_cycle_func(my_list = ['Hello friends'], iteration = int(input("enter iteration: ")))

