count={}
data="hello hai hai"
words=data.split(" ")
for word in words:
    if word not in count:
        count.update({word:1})
    else:
        val=int(count[word])
        val+=1
        count.update({word:val})
print(count)
# another method
str=input("enter string")
wrds=data.split(" ")
for i in wrds:
    count=wrds.count(i)
    dict.update({i:count})
print(count)