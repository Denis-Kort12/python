"""
 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
"""

file = open("out_file.txt", "w")
file.close()

file = open("out_file.txt", "a")

text_write = " "

while text_write != "":
    text_write = input("Введите строку -> ")

    file.write(text_write + "\n")

file.close()
