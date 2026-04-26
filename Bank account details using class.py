class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.amount=self.balance+amount
    def Withdraw(self,amount):
        self.amount=self.balance-amount
    def display(self):
        print(self.name,"balance is:",self.balance)
ba=Bankaccount("CSE",10000)
ba.deposit(1000)
ba.Withdraw(500)
ba.display()
