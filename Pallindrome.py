n=122
num=n
res=0
while n!=0:
    rem=n%10
    n//=10
    res=res*10+rem
if res==num:
    print(f'Given number {num} is Pallindrome')
else:
    print(f'Given number {num} is not Pallindrome')