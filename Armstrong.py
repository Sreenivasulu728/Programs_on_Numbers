n=153
num=n
res=0
p=len(str(n))
while n!=0:
    rem=n%10
    n//=10
    res+=rem**p
if res==num:
    print(f'Given number {num} is Armstrong Number')
else:
    print(f'Given number {num} is not Armstrong Number')