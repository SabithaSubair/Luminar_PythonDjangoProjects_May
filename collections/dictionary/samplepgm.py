dict={'Name':'Zara','Age':7}
print(dict)
print(type(dict))
print("dict['Name']:",dict['Name'])

#key is unique..doesn't aloow repetetion of keys..
# and allow to repeat the values
print("dict['Age']:", dict['Age'])
#to create empty dictionary
#to update
print("updation:")
dict['Age']=9
print(dict)

#to add
print("Add elements")
dict['School']="DPS school"
print(dict)
print("updation")
dict.update({'location':'kochi'})
print(dict)
print("remove")
del dict['Age']
print(dict)
print("all delete")
dict.clear()
print(dict)
print("delete dictionary")
del dict
print(dict)
print("Empty list")
dic={}
print(dic)
#1.mutable
