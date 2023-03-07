n=121
num=n
res=0
while n!=0:
    rem=n%10
    n//=10
    res=res*10+rem
if res==num:
    for x in range(2,res//2+1):
        if res%x==0:
            print(f'Given number {num} is not Polyprime')
            break
    else:
        print(f'Given number {num} is Polyprime')
else:
    print(f'Given number {num} is not Polyprime')
