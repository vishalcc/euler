def isprim(a):
    for i in range(3,int(a**.5)+2):
        if(a%i==0):
            return False
    return True
arr,arrsum=[2,3,5],[2,5,10]
for i in range(6,1000000,2):
    if(isprim(i)):
        arr.append(i)
        arrsum.append(arrsum[-1]+i)

def getconq(j,s):
    global arr,arrsum
    i,s1=0,arrsum[j]
    while(len(arr)>j and arr[j]<=s):
        if(s1==s):
            return (True,i,j)
        elif(s1>s):
            s1-=arr[i]
            i+=1
        else:
            j+=1
            s1+=arr[j]
    return (False,False,False)
g=0
def getind(a,i=0,j=len(arrsum)):
    global arrsum
    mid=(i+j)//2
    if(arrsum[mid]>a and arrsum[mid-1]<=a):
        return mid
    elif(arrsum[mid]>a and arrsum[mid-1]>a):
        return getind(a,i,mid)
    else:
        return getind(a,mid,j)
for i in arr[5:]:
    cond,a,b=getconq(getind(i),i)
    if(cond):
        if(g<b-a+1):
            g=b-a+1
            print(i)
print(g)