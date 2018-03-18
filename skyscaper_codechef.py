for i in range(int(input())):
    x,y=[int(j) for j in (input().split())]
    if x>y:
        print(x-y)
    else:
        print(y-x)
