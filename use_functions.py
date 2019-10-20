"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

account = {'total': 0.0, 'purchases': []}


def enter_money(question, error):

    inp_str = input(question,).strip()
    if inp_str.isnumeric():
        return float(inp_str)
    else:
        print(error)
        return 0.0


def add_funds(account):

    account['total'] += enter_money('Введите сумму пополнения счета: ', 'Ошибка пополнения счета')


def add_purchase(account):

    sum_purchase = enter_money('Введите сумму покупки: ', 'Ошибка ввода суммы покупки')
    if sum_purchase != 0.0:
        if sum_purchase > account['total']:
            print('Недостаточно средств на счете')
            return
        else:
            name_purchase = ''
            while name_purchase == '':
                name_purchase = input('Введите название покупки: ').strip()
                if name_purchase == '':
                    print('Название покупки не может быть пустым')
            account['total'] -= sum_purchase
            account['purchases'].append({'sum': sum_purchase, 'name': name_purchase})


def list_purchases(account):
    print('Ваши покупки:')
    for purchase in account['purchases']:
        print(f'покупка {purchase["name"]:20} на сумму {purchase["sum"]:10.2f}')


while True:
    print(f'У вас с счету {account["total"]: .2f}')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        add_funds(account)
        print()
    elif choice == '2':
        add_purchase(account)
        print()
    elif choice == '3':
        list_purchases(account)
        print()
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
