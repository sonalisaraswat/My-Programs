for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    diff = a[1] - a[0]
    for i in range(1,n-1):
        if a[i+1] - a[i] < diff:
            diff = a[i+1] - a[i]
    print(diff)