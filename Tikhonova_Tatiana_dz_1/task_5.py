# 5.Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

earnings = int(input('введите сумму выручки '))
charge = int(input('введите сумму издержек '))

if earnings > charge:
    profit = int(f'{earnings}') - int(f'{charge}')
    efficiency = profit / earnings
    print('прибыль, рентабельность составила {}'.format(efficiency))
    workers = int(input('введите количество сотрудников фирмы '))
    worker_profit = profit / workers
    print('прибыль фирмы в расчете на одного сотрудника составляет {}'.format(worker_profit))
else:
    print('убыток')
