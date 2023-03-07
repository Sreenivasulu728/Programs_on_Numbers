n=11
for x in range(2,n//2+1):
    if n%x==0:
        print(f'Given number {n} is composit')
        break
else:
    print(f'Given number {n} is not composit')