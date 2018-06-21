for t in range(int(input())):
    a=[]
    s=0
    n, m = [int(i) for i in input().split()]
    o = [int(i) for i in input().split()]
    for i in range(0,n):
        b=[int(j) for j in input().split()]
        a.append(b[1:])
    for i in range(0,m):
        if len(a[o[i]])>0:
            ma=max(a[o[i]])
            s += ma
            a[o[i]].remove(ma)
    print(s)