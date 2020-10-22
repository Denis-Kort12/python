"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

dict_number = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

new_list = []

with open('text.txt', encoding='UTF8') as f:
    for line in f:
        num = line.split(" ")
        new_list.append("{} {} {}".format(dict_number[num[0]], num[1], num[2]))

file = open("text_new.txt", "w", encoding='UTF8')

for item in new_list:
    file.write(item)

file.close()
