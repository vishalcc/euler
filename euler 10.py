import math
prim,i,n=[2],3,0
while(prim[-1]<2000000):
    roots=math.sqrt(i)
    for j in prim:
        if(j>roots):
            break
        if(i%j==0):
            n=1
            continue
    if(n==0):
        prim.append(i)
    i+=2
    n=0
print(prim)