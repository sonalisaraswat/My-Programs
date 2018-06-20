for t in range(int(input())):
    C, D, L=[int(i) for i in input().split()]
    if C>2*D:
        lmi=(C-2*D)*4 + D*4
        lma=C*4+D*4
    else:
        lmi=D*4
        lma=C*4+D*4
    if lmi<=L and lma>=L and L%4==0:
        print("yes")
    else:
        print("no")