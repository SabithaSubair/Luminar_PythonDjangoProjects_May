class Teacher:
    clg_name="cusat"
    def __init__(self,name,id,subject,department):#attributes
        self.name=name#instance variable
        self.id=id
        self.subject=subject
        self.department=department
    def printval(self):
        print("Name::",self.name)
        print("ID::", self.id)
        print("subject::", self.subject)
        print("Department",self.department)
        print("Clg_name::", Teacher.clg_name)
obj1=Teacher("Sabitha",20,"python","cs")
obj1.printval()
