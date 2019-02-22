arr=[1,2,3,4,5,4,5,6,7,8,9]
ans,a=[],[]
def perm(sums=0):
    global ans,a
    if(len(a)==0):
        #print(sums)
        ans.append(sums)
        return
    else:
        i,n=len(a),0
        while(n<i):
            x=a.pop(n)
            perm(sums*10+x)
            a.insert(n,x)
            n+=1
def perm2(sums=0):
    global ans1,a3
    if(len(a3)==0):
        #print(sums)
        ans1.append(sums)
        return
    else:
        i,n=len(a3),0
        while(n<i):
            x=a3.pop(n)
            perm2(sums*10+x)
            a3.insert(n,x)
            n+=1
ans1,a1,a3=[],[1,2,3,4],[]
def combination(i,ind=0):
    global a,arr,ans,a1
    if(i==0):
        perm()
        a1=list(set(arr)-set(a))
        totalcall()
        ans=[]
    else:
        for ind1,val in enumerate(arr[ind:]):
            a.append(val)
            combination(i-1,ind1+1+ind)
            a.pop(-1)
def combination2(i,ind=0):
    global a1,a3
    if(i==0):
        perm2()
    else:
        for ind1,val in enumerate(a1[ind:]):
            a3.append(val)
            combination2(i-1,ind1+1+ind)
            a3.pop(-1)

def totalcall():
    global ans,ll
    #print(a1)
    z12=sorted(a1)
    combination2(1)
    for a in ans:
        for b in ans1:
            c=a*b
            z1,y1=c,b
            l,bl,cl=10,[],[]
            while(b>0 or c>0):
                if(b>0):
                    bl.append(b%10)
                    b=b//10
                if(c>0):
                    cl.append(c%10)
                    c=c//10
            bl.extend(cl)
            bl.sort()

            if(z12==bl):
                print(a,y1,z1)
#[7632,7654,4396,5346,5796,7852,6952,39168,7254]
combination(4)