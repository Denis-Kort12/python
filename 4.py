"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("{} поехала".format(self.name))

    def stop(self):
        print("{} остановилась".format(self.name))

    def turn(self, direction):
        print("{} повернула в {}".format(self.name, direction))

    def show_speed(self):
        print("{} - скорость -> {}".format(self.name, self.speed))


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("{} - TownCar привысила скорость".format(self.name))


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("{} - WorkCar привысил скорость".format(self.name))


class PoliceCar(Car):
    pass


townCar = TownCar(100, 'Черная', 'Городская', False)
sportCar = SportCar(120, 'Серая', 'Спортивная', False)
workCar = WorkCar(130, 'Белая', 'Рабочая', False)
policeCar = PoliceCar(140, 'Синяя', 'Полицейская', True)


townCar.show_speed()
sportCar.show_speed()
workCar.show_speed()
policeCar.show_speed()

townCar.turn('left')
sportCar.turn('right')
workCar.turn('left')
policeCar.turn('right')

townCar.go()
sportCar.stop()

