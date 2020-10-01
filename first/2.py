"""
 Пользователь вводит время в секундах.
 Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
 Используйте форматирование строк.
"""

time_seconds = int(input("Введите время в секундах: "))

hours = time_seconds // 3600
minutes = (time_seconds - 3600 * hours) // 60
seconds = time_seconds - 3600 * hours - 60 * minutes

print("{}:{}:{}".format(hours, minutes, seconds))
