coin=[2,5,10,20,50,100,200]
li=[]
for i in range(201):
    li.append(1)
for rs in coin:
    for ind,val in enumerate(li[rs:]):
        li[ind+rs]+=li[ind]
print(li[-1])