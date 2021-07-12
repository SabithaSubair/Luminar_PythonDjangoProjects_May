#constructor: to initialize instance variables
#constructor:automatically invoke when creating object

class Person:
    def __init__(self,name,age,address):#attributes
        self.name=name#instance variable
        self.age=age
        self.address=address
    def printval(self):
        print("Name::",self.name,"\n","Age::",self.age)
        print("Address",self.address)
obj1=Person("Sabitha",20,"asddf")
obj1.printval()
#another way to i/p read from keyboard
n=input("enter name:")
a=int(input("Age:"))
b=input("Address:")
obj2=Person(n,a,b)
obj1.printval()