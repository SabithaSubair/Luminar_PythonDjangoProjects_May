class Person:
    def value(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)
class Employee(Person):
    def value(self,id,designation,salary):
        self.id=id
        self.designation=designation
        self.salary=sala
        print(self.id)
        print(self.designation)
        print(self.salary)
e=Employee()
e.value("sd",8,"asd")# this call make error....just knoe the concept only..remove this sentence no error
e.value(101,"dssf",100)