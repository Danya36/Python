"""Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка."""

from functools import reduce
def my_func (x,y):
    return x*y
my_list = [y for y in range (99,1001) if y % 2 == 0 ]
print(my_list)
print(reduce(my_func, my_list))
