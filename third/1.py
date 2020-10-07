"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_nums(first_num, second_num):

    if second_num != 0:
        return "\nОтвет: {}".format(first_num/second_num)
    else:
        return "\nДелить на ноль нельзя"


one_num = float(input("Введите перевое число: "))
two_num = float(input("Введите второе число: "))

print(division_nums(one_num, two_num))
