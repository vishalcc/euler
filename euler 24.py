a=[0,1,2,3,4,5,6,7,8,9]
ans,c=[],0
def perm():
    global ans,a,c
    if(len(ans)==10):
        c+=1
        if(c==1000000):
            print(ans)
    else:
        i,n=len(a),0
        while(n<i):
            x=a.pop(n)
            ans.append(x)
            perm()
            ans.pop(-1)
            a.insert(n,x)
            n+=1
perm()