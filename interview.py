s='aaabbccccbaaf'
res=''
count=1
for x in range(len(s)-1):
    if s[x]==s[x+1]:
        count+=1
    else:
        res+=str(count)+s[x]
        count=1
    #res+=str(count)+s[x+1]
res+=str(count)+s[x+1]
print(res)

