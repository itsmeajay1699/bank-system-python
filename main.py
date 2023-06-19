class BankAccount:
    def __init__(self, account_number,account_holder ,balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = int(balance)
    def withdraw(self , money):
        if self.balance >= 0 and self.balance >= money:
            self.balance = self.balance - money;
            return money
    def deposit(self,money):
        self.balance = self.balance + money
        return money
    def currentBalance(self):
        return self.balance

bankAccount = BankAccount(account_number="123456",account_holder="Ajay")

while True:

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        money = int(input("Enter the amount to deposit: "))
        bankAccount.deposit(money)
        print("Your current balance is: ", bankAccount.currentBalance())
    elif choice == 2:
        money = int(input("Enter the amount to withdraw: "))
        bankAccount.withdraw(money)
        print("Your current balance is: ", bankAccount.currentBalance())
    elif choice == 3:
        print("Your current balance is: ", bankAccount.currentBalance())
    elif choice == 4:
        break
    else:
        print("Invalid choice")


