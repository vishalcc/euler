import math
sm=0
def isAmicablenum(a):
    root = math.ceil(a ** .5)
    count = [1]
    if (root * root == a):
        count.append(root)
    for i in range(2, root):
        if (a % i == 0):
            count.append(i)
            count.append(a//i)
    s=sum(count)
    if(s==1):
        return
    root = math.ceil(s ** .5)
    count = [1]
    if (root * root == s):
        count.append(root)
    for i in range(2, root):
        if (s % i == 0):
            count.append(i)
            count.append(s // i)
    global sm
    if(a==sum(count)):
        print(a,s,count)
        if(a!=s):
            sm+=a
for i in range(2,10001):
   isAmicablenum(i)
print(sm)
