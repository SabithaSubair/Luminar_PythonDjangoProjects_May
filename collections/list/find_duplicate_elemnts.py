my_list = [1,1,99,99,8,8,-45]
dup_list = []
print("Duplicate elements are:")
for i in my_list:
  if i not in dup_list:
      dup_list.append(i)
  else:
      print(i)



