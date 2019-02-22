prim,i,n=[2],3,0
while(len(prim)!=10001):
    r=i**.5
    for j in prim:
        if(j>r):
            break
        if(i%j==0):
            n=1
            continue
    if(n==0):
        prim.append(i)
    i+=2
    n=0
print(prim[10000])