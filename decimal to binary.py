n=14
res=0
m=1
while n!=0:
    rem=n%2
    n//=2
    # m*=10
    res=res+rem*m
    m*=10
print(res)