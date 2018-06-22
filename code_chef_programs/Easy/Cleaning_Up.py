for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    a = [i for i in range(1,n+1)]
    re=[int(i) for i in input().split()]
    for i in range(m):
        a.remove(re[i])
    b=a[::2]
    c=a[1::2]
    print(*b, sep=" ")
    print(*c, sep=" ")