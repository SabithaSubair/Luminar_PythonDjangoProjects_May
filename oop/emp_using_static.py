class Employee:
    designation="engineer"
    def setval(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def printval(self):
        print("Id::",self.id,"\n","Name::",self.name,"\n","salary::",self.salary)
        print("Designation is::",Employee.designation)
emp=Employee()
emp.setval(100,"Sabitha",20000)
emp.printval()