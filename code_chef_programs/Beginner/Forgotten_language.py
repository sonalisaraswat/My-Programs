for t in range(int(input())):
    a,b=[int(h) for h in input().split()]
    ar=""
    d=[ch for ch in input().split()]
    for i in range(b):
        ar=ar+input()+" "
    for i in range(a):
        if d[i] in ar:
            print("YES",end=" ")
        else:
            print("NO",end=" ")
    print()