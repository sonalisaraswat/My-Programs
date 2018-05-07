for t in range(int(input())):
    n=int(input())
    a = [i+1 for i in range(n)]
    if n%2==0:
        for i in range(0,n-1,2):
            a[i],a[i+1]=a[i+1],a[i]
    else:
        for i in range(0,n-2,2):
            a[i],a[i+1]=a[i+1],a[i]
        a[n-1],a[n-2]=a[n-2],a[n-1]
    print(*a,sep=" ")