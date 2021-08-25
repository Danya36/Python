"""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк."""

def convert_to_preferred_format (sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return '%02d : %02d : %02d' % (hour, min, sec)
n = int(input ('Введите количество секунд: ' ) )
print ('Время: -', convert_to_preferred_format (n))
