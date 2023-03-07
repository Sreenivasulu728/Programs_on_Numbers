l=[1,2,13,9,6,11]
for i in range(0,len(l)-1):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)