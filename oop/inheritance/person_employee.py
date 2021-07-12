#single inheritence
class Person:#parent class/base class/super class
    def pdetails(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)
class Employee(Person):#derived class/child class/sub class
    def setval(self,id,designation,salary):
        self.id=id
        self.designation=designation
        self.salary=salary
        print("Id::",self.id)
        print("salary::",self.salary)
        print(self.name,"Designation is::",self.designation)
obj=Employee()
obj.pdetails("sabi",30,"asd")
obj.setval(101,"engineer",10000)