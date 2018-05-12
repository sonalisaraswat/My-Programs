for t in range(int(input())):
    n = int(input())
    c = 1
    a = [int(j) for j in input().split()]
    a.sort()
    for i in range(n-1):
        if a[i]!=a[i+1]:
            c+=1
    print(c)    