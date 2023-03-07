l=[1,4,2,6,11,14,13]
for i in range(0,2):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l[-2])