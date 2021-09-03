"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой."""

def info (name, surname, birth_year, city, email, phone_number):
    result = (f'Name: {name}, Surname: {surname}, Year of birth: {birth_year}, City: {city}, Email: {email}, Phone: {phone_number}')
    return result
print(info (input('Enter name: '),
            input('Enter surname: '),
            int(input('Enter year of birth: ')),
            input('Enter city: '), input('Enter email: '),
            int(input('Input telephone: '))))