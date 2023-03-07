n=5
res=0
for x in range(1,n):
    if n%x==0:
        res+=x
if res==n:
    print(f'Given number {n} is Strong Number')
else:
    print(f'Given number {n} is not Strong Number')