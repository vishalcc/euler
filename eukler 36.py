import time
t1=time.time()
def ispalin(a):
    x,z=0,a
    while(z>0):
        x*=10
        x+=z%10
        z=z//10
    if(x!=a):
        return False
    z=int(bin(a).split('b')[1])
    x,a=0,z
    while (z > 0):
        x *= 10
        x += z % 10
        z = z // 10
    if(x!=a):
        return False
    return True
s=0
for i in range(1,1000000,2):
    if(ispalin(i)):
        s+=i
t2=time.time()
print(s,t2-t1)