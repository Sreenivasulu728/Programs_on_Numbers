s='we need to attend class everyday because we need job soon'
l=[]
l=s.split()
d={}
for i in range(0,len(l)):
    if l[i] not in d:
        d[l[i]]=1
    else:
        d[l[i]]+=1
val=list(d.values())
H=val[0]
for i in range(1,len(val)):
    if H<val[i]:
        H=val[i]
for k,v in d.items():
    if H==v:
        print(k)