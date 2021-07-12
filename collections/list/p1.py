# # lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# # lst1=[]
# # [lst1.append(i) for i in lst if i not in lst1]
# # print(lst1)
#
# #
#
# def add(n1,n2):
#     return n1+n2
# def sub(n1,n2):
#     return n1-n2
# def mul(n1,n2):
#     return n1*n2
# def div(n1,n2):
#     return n1/n2
# def floor(n1,n2):
#     return n1//n2
# def expo(n1,n2):
#     return n1**n2
#
# print("Select Operation")
#
# print("1.Addition")
# print("2.Substraction")
# print("3.Multiplication")
# print("4.Division")
# print("5.floor division")
# print("6.Exponent")
# while True:
#     choice=input("Enter a choice")
#     if choice in ('1','2','3','4','5','6'):
#         n1=int(input("Enter the num1:"))
#         n2=int(input("Enter the num:"))
#         if choice=='1':
#             print(add(n1,n2))
#         elif choice=='2':
#             print(sub(n1,n2))
#         elif choice=='3':
#             print(mul(n1,n2))
#         elif choice=='4':
#             print(div(n1,n2))
#         elif choice=='5':
#             print(floor(n1,n2))
#         elif choice=='6':
#             print(expo(n1,n2))
#         break
#     else:
#         print("Invalid")
#
ls=[i for i in range(1,1000) if  i%5==0]
print("Divisible by 5 number between 1 to 1000 is:",ls)