for t in range(int(input())):
    a,b=[int(j) for j in input().split()]
    if a-b == 0:
        print('=')
    elif max(a,b) == a:
        print('>')
    else:
        print('<')
