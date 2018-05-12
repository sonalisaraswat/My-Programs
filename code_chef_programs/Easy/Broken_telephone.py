for t in range(int(input())):
    n = int(input())
    c = 0
    a = [int(j) for j in input().split()]
    if(a[0]!=a[1]):
        c+=1
    if a[n-1]!=a[n-2]:
        c+=1
    for i in range(1,n-1,1):
        if a[i] != a[i+1] or a[i] !=a[i-1]:
            c += 1
    print(c)