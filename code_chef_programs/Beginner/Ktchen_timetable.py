for t in range(int(input())):
    n=int(input())
    c=0
    a=[int(j) for j in input().split()]
    b=[int(j) for j in input().split()]
    if a[0]>=b[0]:
        c+=1
    for i in range(1,n,1):
        if (a[i]-a[i-1])>=b[i]:
            c+=1
    print(c)