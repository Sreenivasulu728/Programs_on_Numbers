n=123456
num=n
res1=0
res2=1
while n!=0:
    rem=n%10
    n//=10
    if rem%2==0:
        res1+=rem
    else:
        res2*=rem
print(f'Sum of even digits in {num} is: {res1}')
print(f'Product of odd digits in {num} is: {res2}')