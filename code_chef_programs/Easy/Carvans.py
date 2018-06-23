for t in range(int(input())):
    ms = 0
    n = int(input())
    a=[int(i) for i in input().split()]
    m = a[0]
    for i in range(1,n):
        if a[i] > m:
            ms += 1
        else:
            if m > a[i]:
                m = a[i]
    print(n - ms)