num={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}
end=9*362880
def getnum(a):
    arr=[]
    while(a>0):
        z=a%10
        arr.append(num[z])
        a=a//10
    return arr
sums=0
for i in range(3,end+1):
    arr=getnum(i)
    if(sum(arr)==i):
        print(i,sums)
        sums+=i

print(sums)