# 4-.Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5.Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
# также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6.Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
from abc import abstractmethod


class ErrorInputData(Exception):
    pass


class Equipment:
    currency = 'руб'

    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.product_data = {}

    def __str__(self):
        return str(f'{self.name} ({self.price} {self.currency}, {self.convert_price_dollar(self.price)}$)')

    def new_product_data(self):
        try:
            name = self.name
            price = int(self.price)
            quantity = int(self.quantity)
            self.product_data = {'название': name, 'кол-во': quantity, 'цена': price}
            return self.product_data
        except Exception as e:
            raise ErrorInputData(f'ErrorInputData: {e}')

    @staticmethod
    def convert_price_dollar(val, src_rate=1, dst_rate=75):
        return val * src_rate / dst_rate

    @classmethod
    def create_converted_price(cls, name, brand, price, src_rate=1, dst_rate=75):
        return cls(name, brand, price, cls.convert_price_dollar(price, src_rate, dst_rate))

    @abstractmethod
    def to_copy_list(self):
        print('запуск печати, используется ', end='')


class Printer(Equipment):
    def __init__(self, name, brand, price, quantity, model):
        super().__init__(name, brand, price, quantity)
        self.model = model

    def to_copy_list(self):
        super().to_copy_list()
        return f'{self.name}'


class Scanner(Equipment):
    def __init__(self, name, brand, price, quantity, color):
        super().__init__(name, brand, price, quantity)
        self.color = color

    def to_copy_list(self):
        super().to_copy_list()
        return f'{self.name}'


class Xerox(Equipment):
    def __init__(self, name, brand, price, quantity, year):
        super().__init__(name, brand, price, quantity)
        self.year = year

    def to_copy_list(self):
        super().to_copy_list()
        return f'{self.name}'


class Storage:
    def __init__(self):
        self.units = []

    def __len__(self):
        return len(self.units)

    def __getitem__(self, item):
        return self.units[item]

    def add(self, unit):
        if not isinstance(unit, Equipment):
            print('ошибка')
            return
        self.units.append(unit)

    @property
    def calc_summary_price(self):
        result = 0
        for unit in self.units:
            result += unit.price
        return result


try:
    product_1 = Printer('принтер', 'Epson', 6939, 5, 'L120')
    product_2 = Scanner('сканер', 'Epson Perfection', 4669, 8, 'grey')
    product_3 = Xerox('ксерокс', 'Xerox', 20294, 4, 2016)
    storage_1 = Storage()
    storage_1.add(product_1)
    storage_1.add(product_2)
    storage_1.add(product_3)
    print(product_1)
    print(product_1.to_copy_list())
    print(len(storage_1))
    print(storage_1.calc_summary_price)
    print(product_1.new_product_data())
    print(product_1.convert_price_dollar(product_1.price))
    print(Equipment.create_converted_price('принтер', 'Epson', 6939))
except ErrorInputData as e:
    print(f'Ошибка: {e}')
except Exception as e:
    print(f'Ошибка: {e}')
