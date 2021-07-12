class Bank:
    def setval(self,account_no,name,deposit,withdraw,balance):
        self.account_no=account_no
        self.name=name
        self.deposit=deposit
        self.withdraw=withdraw
        self.balance=balance
    def printval(self):
        print("Id::",self.account_no,"\n","Name::",self.name)
        print("Deposit::",self.deposit,"\n","Withdrawal::",self.withdraw)
        print("Balance::",self.balance)

ob=Bank()
# ob.setval(100,"Sabitha",20000,1000)
# ob.printval()

n1=int(input("enter account number:"))
n2=input("enter name:")
n3=int(input("enter amount to be deposited:"))
n4=int(input(" enter withdrawal amount:"))
balance=n3-n4
ob.setval(n1,n2,n3,n4,balance)
ob.printval()