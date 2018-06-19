for t in range(int(input())):
    m,n = [int(j) for j in input().split()]
    rx,ry = [int(k) for k in input().split()]
    num=int(input())
    s=input()
    x=y=0
    for i in range(num):
        if s[i]=='L':
            x-=1
        if s[i]=='R':
            x+=1
        if s[i]=='U':
            y+=1
        if s[i]=='D':
            y-=1
    if x==rx and y==ry:
        print("Case %d: REACHED"%(t+1))
    elif x<0 or x>m or y<0 or y>n:
        print("Case %d: DANGER"%(t+1))
    else:
        print("Case %d: SOMEWHERE"%(t+1))
