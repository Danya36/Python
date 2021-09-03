"""'''Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

def my_func(a, b, c):
    sum = a + b + c - min([a, b, c])
    print('Сумма двух наибольших аргументов равна: ', sum)
my_func(int(input('Enter number a: ')),
    int(input('Enter number b: ')),
    int(input('Enter number c: ')))