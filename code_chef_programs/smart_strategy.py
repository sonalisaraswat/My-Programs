for t in range(int(input())):
    n, q = [int(j) for j in (input().split())]
    d = [int(j) for j in input().split()]
    qu = [int (j) for j in input().split()]
    di=1
    for i in range(n):
        di = di * d[i]
    for k in range(q):
        qu[k] = int(qu[k] / di)
    print(*qu, sep = ' ')