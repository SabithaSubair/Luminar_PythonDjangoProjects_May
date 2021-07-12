import re
x="[A-Z]{1}[a-z]"
matcher=re.finditer(x,"Abt c@5kzabc ADFGHkkk anuradha")
for match in matcher:
    print(match.start())
    print(match.group())