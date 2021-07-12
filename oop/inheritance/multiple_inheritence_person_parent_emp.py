class Person:
    def persondetails(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent:
    def parentdetails(self,address):
        self.address = address
        print(self.address)
class Employee(Person,Parent):
    def empdetails(self,id,designation,salary):
        self.id=id
        self.designation=designation
        self.salary=salary
        print(self.id,self.salary,self.designation)
        
ob=Employee()
ob.persondetails("asd",20)
ob.parentdetails("asdd")
ob.empdetails(101,1000,"accountant")