# 2.Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name
        self.summary_textile_cost = []

    @abstractmethod
    def textile_cost(self):
        pass


class Coat(Clothes):
    def __init__(self, name, parameter):
        super().__init__(name)
        self.parameter = parameter

    @property
    def textile_cost(self):
        return self.parameter / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, parameter):
        super().__init__(name)
        self.parameter = parameter

    @property
    def textile_cost(self):
        return 2 * self.parameter + 0.3


class CalcSumClothes:
    def __init__(self):
        self.clothes = []

    def __str__(self):
        return f'общий расход ткани {self.summary}'

    def add(self, cloth):
        if not isinstance(cloth, Clothes):
            print('error')
            return
        self.clothes.append(cloth)

    def __len(self):
        return len(self.clothes)

    @property
    def summary(self):
        result = 0
        for cloth in self.clothes:
            result += cloth.textile_cost
        return result


suit_1 = Suit('red suit', 5)
suit_2 = Suit('white suit', 8)
summary = CalcSumClothes()
summary.add(suit_1)
summary.add(suit_2)
print(suit_1.textile_cost)
print(suit_2.textile_cost)
print(summary)

