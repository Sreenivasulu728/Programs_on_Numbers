l=[1,2,3,4,12,11]
H=l[0]
for i in range(0,len(l)):
    if H<l[i]:
        H=l[i]
print(H)