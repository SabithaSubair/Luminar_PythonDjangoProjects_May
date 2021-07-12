def sumOfPrimes():
    sum = 0
    for a in range(1, 50):
        if a > 1:
            for i in range(2, a):
                if (a % i) == 0:
                    break
            else:
                sum = sum + a
    return sum
print(sumOfPrimes())

#
# # min=int(input("enter initial range"))
# # max=int(input("enter final range"))
# sum=0
# def p(a1,a2):
#  for a in range(a1,a2):
#     if a>1:
#          for i in range(2,a):
#              if(a % i) == 0:
#                  break
#          else:
#              print(a)
#              return (sum+a)
#  p(1,50)
#
