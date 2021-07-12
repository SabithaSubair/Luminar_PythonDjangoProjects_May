import re
print("Rule1")
x="[abc]" #either a,b,c
matcher = re.finditer(x,"abt c@5kzabc")
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())

print("Rule2")
x="[^abc]" #either a,b,c
matcher = re.finditer(x,"abt abvgcsabc")
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
print("Rule3..small letter a-z")
x="[a-z]"
matcher = re.finditer(x,"abt abvASDgcs@#$%abcdghj")
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
print("Rule4..capital A-Z")
x="[a-z]"
matcher = re.finditer(x,"abt abvgcs@#$%abcdASDFGHJghj")
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
print("Rule5...capital and small..a-z A-Z")
x="[A-Za-z]"
matcher = re.finditer(x,"abt abvgfsdgsaSDDcs@#$%abcdASDFGHJghj")
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
print("Rule6....0-9")
x="[0-9]"
matcher = re.finditer(x,"abt abv123457HJghj")
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
#use both a-z and 0-9 and also except case ..ie:^0-9
print("Rule7....check space")
x="\s"
matcher = re.finditer(x,"abt abv Jghj")
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
print("Rule8....check digits")
x="\d"
matcher = re.finditer(x,"ab 12344HJghj")
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
print("Rule9....except digitss")
x="\D"
matcher = re.finditer(x,"ab 12344HJghj")
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
print("Rule8....except words")
x="\W"
matcher = re.finditer(x,"ab addf Jghj")
#print(matcher)
for match in matcher:
    print(match.start())
    print(match.group())
print("Rule8....s")
