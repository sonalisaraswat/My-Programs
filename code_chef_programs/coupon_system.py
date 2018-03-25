for t in range(int(input())):
    d1=0
    d2=0
    d3=0
    c1=0
    c2=0
    c3=0
    for n in range(int(input())):
        c,l,d=[int(j) for j in input().split()]
        if l==1:
            if d>d1:
                d1=d
                c1=c
            if d==d1 and c<c1:
                c1=c
        if l==2:
             if d>d2:
                 d2=d
                 c2=c
             if d == d2 and c < c2:
                 c2 = c
        if l==3:
            if d>d3:
                d3=d
                c3=c
            if d==d3 and c<c3:
                c3=c
    print(d1,c1)
    print(d2,c2)
    print(d3,c3)