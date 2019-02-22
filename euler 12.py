import math
def nums(a):
    root=math.ceil(a**.5)
    count = 2
    if(root*root==a):
        count+=1
    for i in range(2,root):
        z=a%i
        if(z==0):
            count+=2
    if(count>=500):
        print(a,count)
        return True
    else:
        return False
a,i=1,2
while(True):
    a+=i
    i+=1
    if(nums(a)):
        break

#76576500 576 Ans