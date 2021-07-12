class Student:
    def setval(self,name,roll_no,mark,scholl_name):
        self.name=name
        self.roll_no=roll_no
        self.mark=mark
        self.school_name=scholl_name
    def printval(self):
        print("Name::",self.name,"\n","Rollno::",self.roll_no)
        print("Mark::",self.mark,"\n","School_Name::",self.school_name)
st=Student()
a=input("Name is:")
b=int(input("Rollnumber is:"))
c=int(input("Mark is:"))
d=input("School name is:")
st.setval(a,b,c,d)
st.printval()
a1=input("Name is:")
b1=int(input("Rollnumber is:"))
c1=int(input("Mark is:"))
d1=input("School name is:")
st.setval(a1,b1,c1,d1)
st.printval()