"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов
"""


def my_func(first_num, second_num, third_num):
    sum_max = first_num + second_num + third_num - min(first_num, second_num, third_num)

    return sum_max


fst_num = float(input("Введите первое число: "))
sec_num = float(input("Введите второе число: "))
thr_num = float(input("Введите третье число: "))

result = my_func(fst_num, sec_num, thr_num)

print(result)
