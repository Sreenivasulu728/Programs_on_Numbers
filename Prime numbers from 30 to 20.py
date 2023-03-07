for x in range(30,21,-1):
    if x>1:
        for y in range(2,x//2+1):
            if x%y==0:
                break
        else:
            print(x)