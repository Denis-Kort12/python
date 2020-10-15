"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce


list_ready = [num for num in range(100, 1001) if num % 2 == 0]

result_num = reduce(lambda prev_x, x: prev_x*x, list_ready)

print(result_num)
