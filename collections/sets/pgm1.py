#sets........to store elements
set1={1,2,3,5,8,4,1,2}
print(set1)
print(type(set1))
#features
# 1. doesn't store duplicate elements only allow unique elements
# 2. order doesn't keep
# 3. tye is 'set'type
# 4. heterogeneous
# 5. mutable
# 6. not possible nested set...that means eg:set={1,2,3,{4,8}}
set2={}
print(type(set2))
 #above pgm output is  <class 'dict'> so it is dict type
# so create an empty set
s=set()
print(s)
#to add elemenet in set is:
#at a time only one element is add
print("Adding elements in set")
s1=set()
s1.add("hello")
s1.add(3)
s1.add(9.7)
s1.add(True)
print(s1)
# it is heterogenous type becos add defferent type data(datatype ag.int,float,string etc)
# hpomogeneous means same datatype


