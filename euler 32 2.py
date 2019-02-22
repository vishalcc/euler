arr=[1,2,3,4,5,6,7,8,9]
ar=[]
def getd(a,l):
    if(a==0):
        return l
    else:
        l.append(a%10)
        return getd(a//10,l)

for i in range(10,100):
    l9=list(set(arr)-set(getd(i,[])))
    l9.sort()
   # print(l,i1,i)
    for j in range(100,10000):
        c=i*j
        l, bl, cl = c, getd(j,[]), getd(c,[])

        bl.extend(cl)
        bl.sort()
        if (l9 == bl):
            ar.append(l)
#[,[]](2,3,4)
#[]