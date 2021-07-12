class Bank:
    def accntcreate(self,acno,name,bname):
        self.bname=bname
        self.acno=acno
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal
    def depositt(self,amnt):
        self.amnt=amnt
        self.balance+=self.amnt
        print("your",self.bname,"account has been credited with amt",self.amnt)
        print("your current balance=",self.balance)
    def withdraw(self,amt):
        self.amt=amt
        if self.amt>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",self.amt)
            self.balance-=self.amt
            print("available balance=",self.balance)
obj= Bank()
num=int(input("enter account number:"))
obj.accntcreate(num,'abc','sbi')
obj.depositt(2500)
obj.withdraw(1000)
