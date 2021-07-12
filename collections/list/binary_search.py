lst=[1,7,3,9,4,6]
def bsearch():
    lst.sort()
    #print(lst)
    ele=int(input("enter the element:"))
    flag=0
    low=0
    upp=len(lst)-1
    print(upp)
    while low<=upp:
        mid=(low+upp)//2
        #print(mid)
        if ele>lst[mid]:
            low=mid+1
        elif ele<lst[mid]:
             upp=mid-1
        elif ele==lst[mid]:
            flag=1
            break
    if flag==1:
        print("found")
    else:
        print("not found")
bsearch()