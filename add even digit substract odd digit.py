n=12345
num=n
res=0
while n!=0:
    rem=n%10
    n//=10
    if rem%2==0:
        res+=rem
    else:
        res-=rem
print(f'Given number {num} res is: {res}')