for t in range(int(input())):
    n = int(input())
    tot = (n)*(n-1)/2
    a = [int(j) for j in input().split()]
    m = max(a)
    mx1 = a.count(m)
    if a.count(m)>1:
        cor= (mx1-1)*mx1/2
    else:
        a.remove(m)
        m = max(a)
        cor = a.count(m)
    print(cor/tot)