class BankAccount:
    def __init__(self, owner, number, amount, limit):
        self.__owner = owner
        self.__number = number
        self.__amount = amount
        self.limit = limit

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def number(self):
        return self.__number

    @property
    def amount(self):
        return self.__amount

    def withdraw(self, value):
        self.__amount -= value

    def deposit(self, value):
        self.__amount += value

    def transfer(self, value, bank_account):
        self.withdraw(value)
        bank_account.deposit(value)

    @staticmethod
    def bank_code():
        return '001'
