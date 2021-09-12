"""Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

new_file = open('homework5-1.txt', 'w')
print("Enter figures:  ")
while True:
    text = input()
    new_file.write(text + '\n')
    if text == " ":
        break
new_file.close()