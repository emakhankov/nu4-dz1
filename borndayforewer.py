"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

QUESTIONS = [['А.С. Пушкина', 1799, 5, 26]]
MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']


def query_year(person, year):

    # Здесь переопределяем переменную question и используем ее внутри функции
    question = f'Введите год рождения {person} :'
    input_year = input(question).strip()
    while input_year != f'{year}':
        print("Не верно")
        input_year = input(question).strip()


def query_day(person, month, day):

    input_day = input(f'Введите день рождения {person}: ').strip()
    while input_day != f'{day}':
        print("Не верно")
        input_day = input(f'В какой день {MONTHS[month]} родился {person}: ').strip()
    print('Верно')


for question in QUESTIONS:
    query_year(question[0], question[1])
    query_day(question[0], question[2], question[3])