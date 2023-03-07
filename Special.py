n=145
num=n
res=0
while n!=0:
    rem=n%10
    n//=10
    fact=1
    for x in range(1,rem+1):
        fact*=x
    res+=fact
if res==num:
    print(f'Given number {num} is Special Number')
else:
    print(f'Given number {num} is not Special Number')