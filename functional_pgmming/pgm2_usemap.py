products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":10},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},
]
#list all product names
#here use map
print("normal pgm")
name=[]
for product in products:
    name.append(product["item_name"])
print(name)
print("using map")
name=list(map(lambda product:product["item_name"],products))
print(name)
#print outofstock products
# normal pgm
for product in products:
    if product["stock"]==0:
        print("ou of stock product is:",product)

# using filter
out_stock=list(filter(lambda product:product["stock"]==0,products))
print(out_stock)

available=list(filter(lambda product:product["mrp"]<250,products))
print(available)

#print all product details available below <250
#lst=[2,3,4,8,10,7]  o/p=[1,2,3,9,11,8] if num<5 num-1 else num+1