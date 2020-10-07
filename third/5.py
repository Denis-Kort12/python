"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

sum_numbers = 0

while True:
    # Специальный символ !
    str_users = input("Введите строку чисел: ").split(" ")

    if '!' in str_users:
        index_num = str_users.index("!")
        str_users = str_users[:index_num]

        if index_num > 0:
            sum_numbers += sum(map(int, str_users))
            print(sum_numbers)

        exit()

    sum_numbers += sum(map(int, str_users))
    print(sum_numbers)
