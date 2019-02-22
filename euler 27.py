import math
sm=0
def isPrim(a):
    count,n = [2],0
    for i in range(3, a+1,2):
        root=math.ceil(i**.5)
        for j in range(2,root+1):
            if(i%j==0):
                n=1
                break
        if(n==0):
            count.append(i)
        n=0
    return count
arr=isPrim(1000)
arr.reverse()
ans,n1=0,0
def isprim(a):
    if(a<1):
        return False
    if(a==2):
        return True
    for i in range(2,math.ceil(a**.5)+1):
        if(a%i==0):
            return False
    return True
c1,x1,y1=0,0,0
def getcheck(a,b):
    global c1,x1,y1
    c=0
    for n in range(0,b-1):
        c+=1
        if(isprim((n**2)+a*n+b)==False ):
            if(c1<c):
                c1=c
                x1,y1=a,b
            return False

    return True
print(getcheck(-61,971))
for a in range(-1000,1000):

    for b in arr:

        if(getcheck(a,b)):
            #print(a,b)
             if(n1<b):
                print(a,b)
                n1=b
                ans=a*b
print(a,b,c1)