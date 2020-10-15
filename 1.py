"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def get_money(hours, cost, prize):
    return hours * cost + prize


script_name, hours, cost, prize = argv

print("Заработная плата ->", get_money(float(hours), float(cost), float(prize)))
