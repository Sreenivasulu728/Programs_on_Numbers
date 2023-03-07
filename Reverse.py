n=122
num=n
res=0
while n!=0:
    rem=n%10
    n//=10
    res=res*10+rem
print(f'Reverse of {num} is: {res}')