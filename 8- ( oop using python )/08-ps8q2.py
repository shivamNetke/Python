# create account class with 2 attrubutes - balance and account number.
# create method for debit, credit and printing the balance

class Account:
    def __init__(self, bal, accno):
        self.balance = bal
        self.accountNo = accno

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance :", self.getBalance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance :", self.getBalance())


    def getBalance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(500)
acc1.credit(1000)
