
class Bank:
    default_name = ''

    def __init__(self, name=default_name):
        self.name = name
        self.__cash = 0

    def info(self):
        return self.name, self.__cash

    def put_money(self, amount):
        self.__cash += amount

    def withdraw_money(self, amount):
        if self.__cash == 0 or 0 > (self.__cash - amount):
            print('Недостаточно средств для выполнения операции')
        else:
            self.__cash -= amount

    def __del__(self):
        print('Вы отказались от открытия счета,\nлибо закрыли существующий, до свидание')
