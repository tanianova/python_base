# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed
#При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name


    def go(self):
        return f'Машина поехала'

    def stop(self):
        return f'Машина остановилась'

    def turn(self, direction):
        return f'машина повернула {direction}'

    def show_speed(self, speed):
        return f'текущая скорость авто {self.speed}'


class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            return f'вы превысили скорость'
        else:
            return f'текущая скорость городской машины {speed}'


class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            return f'вы превысили скорость'
        else:
            return f'текущая скорость рабочей машины {speed}'


class SportCar (Car):
    pass


class PoliceCar(Car):
    is_police = True


car = Car(100, 'red', 'mazda')
work_car = WorkCar(120, 'black', 'volvo')
town_car = TownCar(150, 'grey', 'bmw')
police_car = PoliceCar(150, 'grey', 'bmw')
print(police_car.is_police)

