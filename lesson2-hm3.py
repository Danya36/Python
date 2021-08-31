"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите номер месяца: "))
if month == 1 or month == 12 or month == 2:
        print("Время года (в dict): ", seasons_dict.get(1))
        print("Время года (в list): ", seasons_list[0])
elif month >= 3 and month < 6:
    print("Время года (в dict): ", seasons_dict.get(2))
    print("Время года (в list): ", seasons_list[1])
elif month >= 6 and month < 9:
    print("Время года (в dict): ", seasons_dict.get(3))
    print("Время года (в list): ", seasons_list[2])
elif month >= 9 and month <= 11:
    print("Время года (в dict): ", seasons_dict.get(4))
    print("Время года (в list): ", seasons_list[3])
else:
        print("Введите номер месяца от 1 до 12")