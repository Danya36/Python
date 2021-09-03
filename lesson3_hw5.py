"""Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""

def my_sum(*numbers):
    sum = 0
    ex = False
    for num in numbers:
        try:
            if num:
                sum += float(num)
        except ValueError:
            ex = True
    return sum, ex

general_sum = 0

while True:
    numbers_string = input("Enter numbers by a space, for exit enter 'q'  ").split(' ')
    sum, ex = my_sum (*numbers_string)
    general_sum += sum
    print(f'Cумма:  {general_sum}')

    if ex:
        break