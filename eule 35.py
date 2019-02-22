s=13
def isprim(a):
    n=0
    for i in range(3,int(a**.5)+2):
        if(a%i==0):
            return False,0
    d = -1
    while a > 0:
        d += 1
        r=a%10
        if(r%2==0 or r%5==0):
            return False,0
        a = a // 10
    return True,d

prim=[]

def rotate(a,d):
    b=a
    while(b>9):
        b=b//10
        r=a%10
        if(r%2==0 or r%5==0):
            return False
        a=r*(10**d)+(a//10)
        if(a not in prim):
           return False
    return True
d=[]
for i in range(101,1000000,2):
    r=isprim(i)
    if(r[0]):
        prim.append(i)
        d.append(r[1])
for i,j in zip(prim,d):
    if(rotate(i,j)):
        s+=1
print(s)
