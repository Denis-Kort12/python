"""
Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def get_data_user(first_name, last_name, birth_date, own_city, email, phone):
    return "\nИмя: {}, Фамилия: {}, Год рождения: {}, Город проживания: {}, Email: {}, Телефон: {}".format(first_name,
                                                                                                           last_name,
                                                                                                           birth_date,
                                                                                                           own_city,
                                                                                                           email, phone)


fst_name = input("Введите имя: ")
lst_name = input("Введите фамилию: ")
bth_date = input("Введите год рождения: ")
city = input("Введите город проживания: ")
eml = input("Введите email: ")
phn = input("Введите телефон: ")

info_data = get_data_user(first_name=fst_name, last_name=lst_name, birth_date=bth_date, own_city=city, email=eml,
                          phone=phn)

print(info_data)
