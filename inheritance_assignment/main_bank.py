from bank.account import savings_acc1, savings_acc2, checking_acc1,checking_acc2
from bank.account import SavingsAccount,CheckingAccount
from bank.transaction import deposit, withdraw, balance_enquiry


accounts = {
    savings_acc1.account_number: savings_acc1,
    savings_acc2.account_number: savings_acc2,
    checking_acc1.account_number: checking_acc1,
    checking_acc2.account_number: checking_acc2

}


def main():
    while True:
        print("Banking System Menu:")
        print("1. Balance Enquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account holder's account_number: ")
            account = accounts.get(account_number)
            if account:
                print("Account Details ")
                print(f"Account Number: {account_number}")
                print(f"account holder name:{account.holder_name}")
                print("Balance for your account:", balance_enquiry(account))
                break
            else:
                print("Account not found.Please Try again or exit")
        elif choice == "2":
            account_number = input("Enter account holder's account_number: ")
            account = accounts.get(account_number)
            if account:
                print("Account Details ")
                print(f"Account Number: {account_number}")
                print(f"account holder name:{account.holder_name}")
                print("Current balance for your account:", balance_enquiry(account))
                amount = float(input("Enter deposit amount: "))
                deposit(account, amount)
                print("Deposit successful.")
                print("new balance for your account: ", balance_enquiry(account))
                break
            else:
                print("Account not found.Please Try again or exit")
        elif choice == "3":
            account_number = input("Enter account holder's account_number: ")
            account = accounts.get(account_number)
            if account:
                print("Account Details ")
                print(f"Account Number: {account_number}")
                print(f"account holder name:{account.holder_name}")
                print("Current balance for your account:", balance_enquiry(account))
                amount = float(input("Enter withdrawal amount: "))
                withdraw(account, amount)
                print("Withdrawal successful.")
                print("new balance for your account: ", balance_enquiry(account))
                break
            else:
                print("Account not found.Please Try again or exit")
        elif choice == "4":
            print("Exiting the banking system.")
            break
        else:
            print("Invalid choice. Please try again.\n")



main()
