for t in range(int(input())):
    l ,k=[int(j) for j in input().split()]
    a = l-k+1
    if k>l:
        print("Case %d: 0"%(t+1))
    else:
        print("Case %d:"%(t+1),(a*(a+1))//2)