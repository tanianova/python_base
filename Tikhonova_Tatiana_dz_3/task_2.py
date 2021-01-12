# 2.Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год
# рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def user_profile(name, surname, birthday, city, email, phone, **kwargs):
    print(f'имя: {name}, фамилия: {surname}, дата рождения: {birthday},'
          f' город проживания: {city}, email: {email}, телефон: {phone}')
    if kwargs:
        print(f'дополнительная информация: ', end='')
        for key, val in kwargs.items():
            print(f'{key} : {val}', end=', ')


user_1 = {
    'name': 'Татьяна',
    'surname': 'Тихонова',
    'birthday': 1992,
    'city': 'Москва',
    'email': 'tanianova@yandex.ru',
    'phone': 12345678
}

user_profile(marriage='да', email='tanianova@yandex.ru', name='Татьяна', birthday=1992,
             surname='Тихонова', city='Москва', phone=12345678, children='нет')
