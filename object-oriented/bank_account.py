class BankAccount:
    def __init__(self, owner, number, amount, limit):
        self.number = number
        self.owner = owner
        self.amount = amount
        self.limit = limit

    def show_amount(self):
        print(f'The owner {self.owner} has amount of {self.amount}')
