for t in range(int(input())):
    a=[int(j) for j in input().split()]
    m=max(a)
    if a[0]==m:
        a[0]=-1
    if a[1]==m:
        a[1]=-1
    if a[2]==m:
        a[2]=-1
    print(max(a))