term,a,b=2,1,1
import sys
sys.setrecursionlimit(1500)
def getdig(a,n=0):
    if(a==0):
        return n
    else:
        return getdig(a//10,n+1)
while True:
    if(getdig(b)==1000):
        print(term)
        break
    a,b=b,a+b
    term+=1