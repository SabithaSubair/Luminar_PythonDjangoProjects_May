# quantifiers
# x='a+' a including group
# x='a*' count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2}' 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a' check starting with a
# x='a$' check ending with a
import re
print("a including group")
x="a+"
r="aaa abc aaaa cga"
matcher = re.finditer(x,r)
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())

print("count including zero number of a")
x="a*"
r="aaa abc aaaa cga"
matcher = re.finditer(x,r)
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())

print("a? count a as each including zero no of a")
x = "a?"
r = "aaa abc aaaa cga"
matcher = re.finditer(x, r)
# print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())

print("'a{2}' 2 no of a position")
x = "a{2}" #we use any no at the place of 2 ....eg:a{3},a{4} etc
r = "aaa abc aaaa cga"
matcher = re.finditer(x, r)
# print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())

print("'a{2,3}' minimum 2 and maxm 3 no of a position")
x = "a{2,3}" #we use any no at the place of 2,3 ....
r = "aaa abc aaaa cga"
matcher = re.finditer(x, r)
# print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())

print("^a check starting with a")
x = "^a"
r = "aaa abc aaaa cga"
matcher = re.finditer(x, r)
# print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())

print("a$ check ending with a")
x = "a$"
r = "aaa abc aaaa cga"
matcher = re.finditer(x, r)
# print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())