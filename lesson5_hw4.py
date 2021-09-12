"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""


translater = {'One' : 'Odin', 'Two': 'Dva', 'Three': 'Tri', 'Four': 'Chetyri'}
result = []
with open('homework5-4.txt', 'r') as file:
    for line in file:
        row = line.split(" - ")
        print(row)
        if row[0] in translater:
            word = translater[row[0]]
            result.append(word + ' - ' + row[1])
        print(result)

new_file = open("homework5-4-result.txt", "w")
new_file.writelines(result)
new_file.close()

