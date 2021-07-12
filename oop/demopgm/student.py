class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
         print(self.name)
         print(self.age)
    def __str__(self):
        return self.name
f1=open('student','r')
for line in f1:
    data=line.rstrip("\n").split(",")
    print(data)
    name=data[0]
    age=data[1]
    obj=Person(name,age)
    print(obj)
    obj.printvalue()
    #print(obj)