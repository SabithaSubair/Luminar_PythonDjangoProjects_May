class College:
    def cvalue(self,name,place):
        self.name=name
        self.place=place
        print(self.name,self.place)
class Department(College):
    def dvalue(self,branch):
        self.branch = branch
        print(self.branch)
class Student(Department):
    def svalue(self, rolno, mark):
        self.rolno = rolno
        self.mark = mark
        print(self.rolno, self.mark)

class Subject():
    def subvalue(self,sub_name):
        self.sub_name=sub_name
        print(self.sub_name)

class Teacher(College,Subject):
    def tvalue(self,tid):
        self.tid=tid
        print(self.tid)


# object creation and calling in single inheritence
ob1=Department()
ob1.dvalue("Computer Science")
ob1.cvalue("rset","kakkanad")
# object creation and calling in multilevel inheritence

ob2=Department()
ob2.dvalue("mech")
ob2.cvalue("rset","kakkanad")

ob3=Student()
ob3.svalue(4,78)
ob3.dvalue("it")
ob3.cvalue("cusat","kalamassery")

# object creation and calling in multiple inheritence
ob4=Teacher()
ob4.cvalue("amaljyothy","kanjirappally")
ob4.subvalue("python")

