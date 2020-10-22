"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

file = open("text_num.txt", "w")

text_write = input("Введите строку чисел -> ")

file.write(text_write)

file.close()

with open('text_num.txt', encoding='UTF8') as f:
    for line in f:
        list_num = line.split()


sum_num = 0

for item in list_num:
    sum_num += int(item)

print("Сумма чисел:", sum_num)

