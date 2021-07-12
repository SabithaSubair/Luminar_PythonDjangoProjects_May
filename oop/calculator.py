class Calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def add(self):
        return self.n1 + self.n2

    def sub(self):
        return self.n1 - self.n2

    def mul(self):
        return self.n1 * self.n2
    def div(self):
        return self.n1/self.n2


a=int(input("Num1:"))
b= int(input("Num2:"))
ob=Calculator(a,b)
print(ob.add())
print(ob.sub())
print(ob.mul())
print(ob.div())
