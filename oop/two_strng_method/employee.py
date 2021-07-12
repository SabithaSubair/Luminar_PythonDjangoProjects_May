class Employee:
    company_name="ASD"
    def __init__(self,name,id,salary,experience):
        self.name=name
        self.id=id
        self.salary=salary
        self.experience=experience
    def printdet(self):
        print(self.name,self.id,self.salary,self.experience.Employee.company_name)
    def __str__(self):
        return self.name+str(self.experience)
e=Employee("amal",2,20000,4)
print(e)
