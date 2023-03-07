n=135
num=n
res=0
p=len(str(n))
while n!=0:
    rem=n%10
    n//=10
    res+=rem**p
    p-=1
if res==num:
    print(f'Given number {num} is Disarm Number')
else:
    print(f'Given Number {num} is not Disarm Number')