a=2**1000
def getsum(a,sums=0):
    if(a==0):
        print(sums)
    else:
        sums+=a%10
        getsum(a//10,sums)
getsum(a)