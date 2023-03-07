for x in range(20,31):
    if x>1:
        for y in range(2,x//2+1):
            if x%y==0:
                break
        else:
            print(f'Prime number in given range: {x}')
