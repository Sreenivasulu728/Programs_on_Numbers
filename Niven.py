n=131
num=n
res=0
while n!=0:
    rem=n%10
    n//=10
    res+=rem
if num%res==0:
    print(f'Given number {num} is niven number')
else:
    print(f'Given number {num} is not niven number')

    