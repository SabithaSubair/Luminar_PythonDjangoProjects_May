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

    def __str__(self):
        return self.name
f1=open('work2','r')
for line in f1:
    data=line.rstrip("\n").split(",")
    # print(data)
    name=data[0]
    roll=data[1]
    course=data[2]
    mark=data[3]
    obj=Student(name,roll,course,mark)
    print(obj)
    obj.printvalue()
    #print(obj)