class Employee:
    def setval(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary
    def printval(self):
        print("Id::",self.id,"\n","Name::",self.name,"\n","Designation::",self.designation,"\n","salary::",self.salary)

emp=Employee()
emp.setval(100,"Sabitha","Developer",20000)
emp.printval()
print("another way..")
n1=int(input("enter id:"))
n2=input("enter name:")
n3=input("enter designation:")
n4=int(input(" enter salary"))
emp.setval(n1,n2,n3,n4)
emp.printval()