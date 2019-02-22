def getday(year):
    if(year%4!=0 or (year%100==0 and (year//100)%4!=0)):
        return 365
    else:
        return 366
ly={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
y={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
sun=0
days=6
for i in range(1901,2001):
    x=getday(i)
    if(x==365):
        for k,v in y.items():
            if(days==1):
                sun+=1
            days=7-(v-days)%7
    else:
        for k,v in y.items():
            if(days==1):
                sun+=1
            days=7-(v-days)%7
print(sun)