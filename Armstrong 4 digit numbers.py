for n in range(1000,10000):
    num=n
    res=0
    p=len(str(n))
    while n!=0:
        rem=n%10
        n//=10
        res+=rem**p
    if res==num:
        print(res)