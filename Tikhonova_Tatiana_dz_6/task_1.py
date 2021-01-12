# 1.Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
# на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    def running(self):
        i = 0
        while i < len(self.__color):
            print(f'загорелся {self.__color[i]} цвет')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                sleep(7)
            i += 1


user_1 = TrafficLight()
user_1.running()
