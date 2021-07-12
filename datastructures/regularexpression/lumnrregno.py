import re
f2=open('pythonbatch','w')
rule="([L][U][M]\d{2}[P][Y]\d{3}$)"
f1=open('lumnregno','r')
for num in f1:
    number=num.rstrip("\n")
    matcher = re.fullmatch(rule, number)
    if matcher is not None:
       f2.write(number)
       f2.write("\n")