# 17) Create a class BankAccount with private attributes balance and account_number.
#  Implement methods deposit() and withdraw() to modify the balance. Ensure that the
#  balance cannot be accessed directly from outside the class.

class BankAccount:
    def __init__(self,account_number,balance=0):
        self.balance=balance
        self.account_number=account_number
        
    def deposit(self,deposit_amount):
        self.balance=self.balance+deposit_amount
        print("Successfull deposited")

    def withdraw(self,withdraw_amount):
        if self.balance<=0:
            print("low balance")
        else:
            self.balance=self.balance-withdraw_amount
            print("Successfull withdraw")

p1=BankAccount(5000,1000001)
p1.deposit(500)
p1.withdraw(500)