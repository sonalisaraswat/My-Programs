t=int(input())
for i in range(t):
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    a.sort(reverse=True)
    g=0
    g1=0
    if(n-k>=k):
        for i in range(n-k):
            g+=a[i]
        g1+=sum(a[n-k:])
    else:
        for i in range(k):
            g+=a[i]
        g1+=sum(a[k:])
    print(g-g1)