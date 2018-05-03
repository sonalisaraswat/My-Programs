for t in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    ep = p = 0
    for i in range(n-1):
        if a[i]>a[i+1]:
            ep+=1
        for j in range(i+1,n,1):
            if a[i]>a[j]:
                p+=1
    if ep!=p:
        print("NO")
    else:
        print("YES")