import sys
from bank import Bank

if __name__ == '__main__':
    client = Bank()
    print('Добро пожаловать в БАНК!')
    name = input('Введите ваще Имя: ')
    client.name = name
    check_yes = {'yes', 'y', 'да', 'д'}
    check = input('Хотите открыть счет (Да/Нет):')

    if check.lower() in check_yes:
        print('У Вас на счету: ', client.info()[1])
    else:
        sys.exit()
    while True:
        print('Выберите тип операции\n1 - добавить сумму на счет\n2 - снять сумму\n3 - закрыть счет')
        check_operation = input('Введите номер операции: ')

        if check_operation == '3':
            break

        elif check_operation == '1':
            put_amount = int(input('Введите сумму: '))
            client.put_money(put_amount)
            print('У Вас на счету: ', client.info()[1])
        elif check_operation == '2':
            pull_amount = int(input('Введите сумму: '))
            client.withdraw_money(pull_amount)
            print('У Вас на счету: ', client.info()[1])
        else:
            print('Неверный ввод номера операции')







            

