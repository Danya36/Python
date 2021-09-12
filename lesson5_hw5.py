"""5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

my_numbers = ('5 78 45 67 34 54 2 6')
my_files = open('homework5-5.txt' , 'w')
my_files.write(my_numbers)

my_files = open('homework5-5.txt' , 'r')
list = my_files.read().split()
sum = 0
for i in list:
    sum += int(i)
print ('The sum o the numbers: ', sum)
my_files.close()


