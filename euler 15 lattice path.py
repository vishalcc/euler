arr=[]
x=21
for i in range(x):
    arr.append([])
    for j in range(x):
        if(i==0 or j==0):
            arr[i].append(1)
        else:
            arr[i].append(0)
n=0
for i in arr[1:]:
    n+=1
    for j in range(1,x):
        arr[n][j]=arr[n][j-1]+arr[n-1][j]
for i in arr:
    print(i)