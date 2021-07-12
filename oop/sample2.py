#using attributes
class Person:
    def setval(self,name,age):#attributes
        self.name=name#instance variable
        self.age=age
    def printval(self):
        print("Name::",self.name,"\n","Age::",self.age)
obj1=Person()
obj1.setval("Sabitha",20)
obj1.printval()
print("another way..")
n=input("enter name:")
a=int(input("Age:"))
obj1.setval(n,a)
obj1.printval()