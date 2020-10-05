"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()
"""

elements_input = input("Ввод элементов списка: ")

list_elements = elements_input.split(" ")

for i in range(0, len(list_elements) - 1, 2):
    list_elements[i], list_elements[i+1] = list_elements[i+1], list_elements[i]

print(list_elements)


