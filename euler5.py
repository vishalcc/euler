prim,n=[2],0
for i in range(3,21,2):
    for j in prim:
        if(i%j==0):
            n=1
            continue
    if(n==0):
        prim.append(i)
    n=0
mins=1
for i in prim:
    mins*=i
for i in range(4,21):
    if(mins%i!=0):
        a=mins%i
        m=i//a
        mins*=m
print(mins)