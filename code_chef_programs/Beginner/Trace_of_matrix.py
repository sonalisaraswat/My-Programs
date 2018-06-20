for t in range(int(input())):
    n=int(input())
    ma=[]
    for j in range(n):
        mi=[int(i) for i in input().split()]
        ma.append(mi)
    sum= s1=s2=0
    for i in range(n):
        sum+=ma[i][i]
    for i in range(1,n):
        s1=s2=0
        for j in range(n-i):
            s1+=ma[j+i][j]
            s2+=ma[j][j+i]
        if s1>sum:
            sum=s1
        if s2>sum:
            sum=s2
    print(sum)