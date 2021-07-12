f1=open('count','r')
count={}
for i in f1:


 words=i.split(" ")
 #print(words)
 for word in words:
    if word not in count:
        count.update({word:1})
    else:
        val=int(count[word])
        val+=1
        count.update({word:val})
print(count)

