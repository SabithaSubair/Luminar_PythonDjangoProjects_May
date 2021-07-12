class Student:
    def __init__(self,name,roll,course,mark):
        self.name=name
        self.roll=roll
        self.course=course
        self.mark=mark
    def printvalue(self):
         print(self.name)
         print(self.roll)
         print(self.course)
         print(self.mark)
lst=[]
f=open('sample','r')
for i in f:
    d=i.rstrip("\n").split(",")
    print(d)
    name=d[0]
    roll=d[1]
    course=d[2]
    mark=d[3]
    obj=Student(name,roll,course,mark)
    # print(obj)
    obj.printvalue()
    lst.append(obj)
#print(lst)
mark=[]
for st in lst:
    mark.append(st.mark)
print(mark)
for st in lst:
    if (st.mark==max(mark)):
        print("Maximum mark:",st.roll,st.name,st.course,st.mark)
