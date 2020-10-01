"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int(input("Введите число: "))

if number <= 0:
    print("число должно быть положительным")
    exit()

max_num = number % 10
number = number // 10

while number != 0:
    number_check = number % 10

    if max_num < number_check:
        max_num = number_check

    number = number // 10

print("Самое большое число:", max_num)
