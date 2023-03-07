l=[1,2,3,4,5,6,7,8]
list1=[]
list2=[]
for i in range(0,len(l)):
    if l[i]%2==0:
        list1.append(l[i])
    else:
        list2.append(l[i])
print(list1+list2)