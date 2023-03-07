for n in range(100,1000):
    num=n
    res=0
    p=len(str(n))
    while n!=0:
        rem=n%10
        n//=10
        res+=rem**p
        p-=1
    if res==num:
        print(res)