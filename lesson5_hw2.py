"""Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке."""

file = open('homework5-2.txt', 'r')
words = file.read()
print(f'File contents: \n {words}')

file = open('homework5-2.txt')
line_count = 0
for line in file:
    line_count += 1
print("Numbers of rows: ", line_count)

file = open('homework5-2.txt')
words = file.readlines()
for i in range(len(words)):
    print (f'{len(words[i])} character in {i + 1} row')

file.close()
