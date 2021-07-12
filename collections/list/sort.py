# print("sorting")
# lst1=[1,2,6,9,3,0,5,-9,-4]
# lst1.sort()
# print(lst1)

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
