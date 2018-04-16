for t in range(int(input())):
    n,k=[int(j) for j in input().split()]
    al=[int(j) for j in input().split()]
    b1=[int(j) for j in input().split()]
    m=max(b1)
    s=0
    for i in range(n):
        if al[i]<(m+1):
            s=s+(m+1-al[i])
    print(s*k)