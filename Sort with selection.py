l=[1,2,3,4,5,11,13]
for i in range(0,len(l)-1):
    min=i
    for j in range(i+1,len(l)):
        if l[min]>l[j]:
            l[min],l[j]=l[j],l[min]
print(l)