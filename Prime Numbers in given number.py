n=987645
num=n
while n!=0:
    rem=n%10
    n//=10
    if rem>1:
        for x in range(2,rem//2+1):
            if rem%x==0:
                break
        else:
            print(f'Prime Numbers in {num} is :{rem}')
