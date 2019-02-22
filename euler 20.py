a=1
for i in range(2,100):
    a*=i
def getsum(a,sum=0):
    if(a==0):
        print(sum)
    else:
        sum+=a%10
        getsum(a//10,sum)
getsum(a)