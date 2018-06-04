for t in range(int(input())):
    n, k = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    di=int((n+k)/2)
    a.sort()
    print(a[di])