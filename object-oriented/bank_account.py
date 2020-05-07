class BankAccount:
    def __init__(self, owner, number, amount, limit):
        self.__number = number
        self.__owner = owner
        self.__amount = amount
        self.__limit = limit

    def show_amount(self):
        print(f'The owner {self.__owner} has amount of {self.__amount}')

    def withdraw(self, value):
        self.__amount -= value

    def deposit(self, value):
        self.__amount += value

    def transfer(self, value, bank_account):
        self.withdraw(value)
        bank_account.deposit(value)
