



class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)


class CheckingAccount(Account):
    pass



savings_acc1 = SavingsAccount("SA123", "Jerry", 1000,6)
savings_acc2 = SavingsAccount("SA456", "Sharon", 1500,6)
checking_acc1 = CheckingAccount("CA789", "Jonathan", 2000)
checking_acc2 = CheckingAccount("CA999", "Sefali", 20000000)