p=input("enter element:")
c={}
for i in p:
    if i not in c:
        c.update({i:1})
    else:
        print("first recursive element:",i)
        break
#another method
# x=input("enter a string ")
# count=0
# for i in x:
#     count=x.count(i)
#     if count > 1:
#         break
# print("first recursive element is",i)
