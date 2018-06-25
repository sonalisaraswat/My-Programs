for t in range(int(input())):
    n=int(input())
    maxL = 0
    p=[]
    pi=[]
    L = [int(i) for i in input().split()]
    R = [int(i) for i in input().split()]
    for j in range(n):
        L[j] = (L[j] * R[j])
        if L[j] > maxL:
            maxL=L[j]
    if L.count(maxL) == 1:
         print(L.index(maxL)+1)
    else:
        for i in range(n):
            if L[i] == maxL:
                p.append(R[i])
                pi.append(i+1)
        print(pi[p.index(max(p))])

