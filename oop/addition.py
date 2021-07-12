class Add():
    def setval(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def printval(self):
        print(self.n1+self.n2)
obj1=Add()
obj1.setval(10,20)
obj1.printval()
obj1.setval(18,5)
obj1.printval()
obj1.setval(10,6)
obj1.printval()