my_list = [1,4,3,8,5,88,55,99,-99,-45]
new_list = []

while my_list:
  min = my_list[0]
  for i in my_list:
      if i<min:
            min=i

  new_list.append(min)
  my_list.remove(min)
print("sorted order is:",new_list)
print("minimum no:",new_list[0])
print("maximum no:",new_list[-1])

#another method
# my_list = [1,4,3,8,5,88,55,99,-99,-45]
# my_list.sort()
# print("minimum no:",my_list[0])
# print("maximum no:",my_list[-1])
