"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('text.txt') as f:
    text = f.readlines()
    len_text = len(text)

for i, line in enumerate(text):
    count_words = len(line.split(" "))
    print("Колличество слов в {} строке -> {}".format(i + 1, count_words))

print("Колличество строк ->", len_text)
