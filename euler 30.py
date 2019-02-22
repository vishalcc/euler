def getsums(a,sums=0):
    if(a==0):
        return sums
    else:
        sums+=(a%10)**5
        return getsums(a//10,sums)
s=0
for i in range(2,1000000):
    if(getsums(i)==i):
        print(i)
        s+=i
print(s)