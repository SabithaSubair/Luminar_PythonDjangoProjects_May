#lst=[2,3,4,8,10,7]  o/p=[1,2,3,9,11,8] if num<5 num-1 else num
lst=[2,3,4,8,10,7]
print("using map function")
result=list(map(lambda num:num+1 if num>=5 else num-1,lst))
print(result)