
def deposit(account, amount):
    account.deposit(amount)


def withdraw(account, amount):
    account.withdraw(amount)


def balance_enquiry(account):
    return account.get_balance()