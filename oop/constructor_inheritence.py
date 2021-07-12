class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)

class Student(Person):
    def _init_(self,rollno,mark,name,age):
        super()._init_(name,age)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print("rollno",self.rollno)
        print("mark",self.mark)

s=Student(2,34,"anu",22)
s.printval()
s.print()