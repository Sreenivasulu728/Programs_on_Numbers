n=12
if n>1:
    for x in range(2,n//2+1):
        if n%x==0:
            print(f'Given number {n} is not Prime')
            break
    else:
        print(f'Given number {n} is Prime')
else:
    print(f'Given number {n} is not Prime')