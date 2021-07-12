a=input("Enter string:")
vowels = "a,e,i,o,u,A,E,I,O,U"
c = 0
for i in a:
    if i in vowels:
        c = c + 1
if c==0:
    print("No wowels")
else:
    print("No of wowels are:",c)
