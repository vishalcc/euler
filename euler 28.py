arr=[]
n=1001
for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(0)
def spiralMatrix():
    global arr
    row,l=1,len(arr)
    lhalf=l//2
    arr[lhalf][lhalf]=1
    starti,startj=lhalf,lhalf+1
    sums=2
    for i1 in range(lhalf):
        for j1 in range(4):
            if(j1==0):
                for i in range(starti,lhalf+row+1):
                    arr[i][startj]=sums
                    sums+=1
                starti=lhalf+row
            elif(j1==1):
                for j in range(lhalf+row-1,lhalf-row-1,-1):
                    arr[starti][j]=sums
                    sums+=1
                startj=lhalf-row
            elif(j1==2):
                for i in range(lhalf+row-1,lhalf-row-1,-1):
                    arr[i][startj]=sums
                    sums+=1
                starti=lhalf-row

            elif(j1==3):
                for j in range(lhalf-row+1,lhalf+row+1):
                    arr[starti][j]=sums
                    sums+=1
                row+=1
                startj=lhalf+row
    s=0
    for ind,i in enumerate(arr):
        s+=i[ind]
        s+=i[l-1-ind]
        if(ind==l-1-ind):
            s-=i[ind]
    print(s)
spiralMatrix()