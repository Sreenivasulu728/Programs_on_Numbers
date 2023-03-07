n=234
res=0
num=n
while n!=0:
    rem=n%10
    n//=10
    res+=rem
print(f'Sum of {num} is: {res}')