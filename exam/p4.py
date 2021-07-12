class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address


class Employee(Person):

    def emp_printval(self):
        print("Name::",self.name,"\n","Age::",self.age)
        print("Address",self.address)


emp=Employee("sabi",20,"hasbdhgsxdg")
emp.emp_printval()



