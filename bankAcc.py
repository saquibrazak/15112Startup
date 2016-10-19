class BankAccount:
    AccountNum = 1
    def __init__(self,b,tp, iban):
        self.accountNumber = BankAccount.AccountNum
        BankAccount.AccountNum = BankAccount.AccountNum + 1
        self.balance = b
        self.type = tp
        self.IBAN = iban
    def __str__(self):
        result = str(self.accountNumber)+":"+str(self.balance)+":"+str(self.type)
        return result
    def __repr__(self):
        return self.__str__()
    def deposit(self,amount):
        self.balance = self.balance + amount
    def withdraw(self,amount):
        if self.balance < amount:
            return 0
        self.balance = self.balance - amount
        return amount
    def transfer(self,toAccount,amount):
        amnt = self.withdraw(amount)
        toAccount.deposit(amnt)
    
acc1 = BankAccount(1000.5,"S","something")
print acc1

acc2 = BankAccount(2000,"C","something different")
print acc2

acc1.deposit(50000)
acc1.transfer(acc2,10000)
print acc1
print acc2










 
