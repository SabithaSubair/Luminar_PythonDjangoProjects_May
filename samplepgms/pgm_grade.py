a=int(input("enter the mark for english:"))
b=int(input("enter the mark for maths:"))
c=int(input("enter the mark for chemisty:"))
d=int(input("enter the mark for physics:"))
e=int(input("enter the mark for biology:"))
f=a+b+c+d+e
print("students Total Score:",f)
g=f/5
print("Average Mark : ",g)
if f>90:
    print("A+")
elif 80<f<90:
    print("A")
elif 70<f<80:
    print("B+")
elif 60<f<70:
    print("B")
elif 50<f<60:
    print("C+")
elif 40<f<50:
    print("C")
else:
    print("Failed")
