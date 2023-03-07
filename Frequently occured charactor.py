l=[10,0,7,8,0,5,0,7,11]
for i in range(0,len(l)):
    for j in range(i+1,len(l)-i-1):
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)