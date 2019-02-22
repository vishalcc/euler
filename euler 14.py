count,num=1,1
def works(i):
    global count
    coun=0
    while(True):
        if(i==1):
            coun+=1
            if(count<coun):
                count=coun
                return True
            return False
        if(i%2==0):
            i=i>>1
        else:
            i=3*i+1
        coun+=1

for i in range(2,1000001):
    if(works(i)):
        num=i
#837799,525
