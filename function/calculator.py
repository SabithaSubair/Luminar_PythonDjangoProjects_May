
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2
print("Select Operation")

print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
while True:
    choice=input("Enter a choice")
    if choice in ('1','2','3','4'):
        n1=int(input("Enter the num1:"))
        n2=int(input("Enter the num:"))
        if choice=='1':
            print(add(n1,n2))
        elif choice=='2':
            print(sub(n1,n2))
        elif choice=='3':
            print(mul(n1,n2))
        elif choice=='4':
            print(div(n1,n2))
        break
    else:
        print("Invalid")

