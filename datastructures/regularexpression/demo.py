#regular expression.....re=>package of pattern matching
#use in validation


import re  #re is a package
count=0
matcher = re.finditer('ab','abaabbab')
#print(matcher)
for match in matcher:
    print("match available at:",match.start())#return positions
    print("group:",match.group()) #which o ject find match
    count+=1
print("count=",count)
