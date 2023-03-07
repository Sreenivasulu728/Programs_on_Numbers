l=[1,1,2,3,2,4]
res=[]
for i in range(0,len(l)):
    if l[i] not in res:
        res.append(l[i])
print(res)