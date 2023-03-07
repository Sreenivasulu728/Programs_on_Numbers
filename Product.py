n=234
res=1
num=n
while n!=0:
    rem=n%10
    n//=10
    res*=rem
print(f'Product of {num} is: {res}')
