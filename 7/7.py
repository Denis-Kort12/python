"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

dict_data = {}

with open("data.txt", encoding="UTF8") as f:
    for line in f:
        temp = line.split()
        dict_data[temp[0]] = temp[1:]

print(dict_data)

dict_result = {}
all_profit = 0
i = 0

for key, name in dict_data.items():

    profit = int(name[1]) - int(name[2])

    if profit > 0:
        i += 1
        all_profit += profit

    dict_result[key] = profit

mid_profit = all_profit / i

list_company = []

list_company.append(dict_result)
list_company.append({"average_profit": mid_profit})

print(list_company)

with open("file.json", "w") as write_f:
    json.dump(list_company, write_f)
