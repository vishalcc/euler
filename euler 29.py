arr=[]
for a in range(2,101):
    for b in range(2,101):
        arr.append(a**b)
print(len(set(arr)))