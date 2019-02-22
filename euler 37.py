def isprim(a):
    z=a
    while(z>0):
        x1=z%10
        if(x1%2==0 or x1%5==0 or x1==1):
            return False
        z=z//10
    for i in range(3,int(a**.5)+2):
        if(a%i==0):
            return False
    return True
def isprim2(a):
    for i in range(3,int(a**.5)+2):
        if(a%i==0):
            return False
    return True
s,c=0,0
def callme(a):
    s1,d=0,10
    while(a>0):
        if(d>a):
            break
        if(isprim2(a%d)):
            d *= 10
            continue
        else:
            return False
    return True
for i in range(9,1000000,2):
    if(isprim(i)):
        if(callme(i)):
            c+=1
            print(i)
            if(c==11):
                break
            s+=i
print(s)