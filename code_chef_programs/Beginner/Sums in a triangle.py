t = int(input())
r = []
for i in range(t):
    n = int(input())
    l = []
    for j in range(n):
        l.append([int(c) for c in input().split()])
    for k in range(len(l) - 2, -1, -1):
        for m in range(len(l[k])):
            l[k][m] = l[k][m] + max(l[k + 1][m], l[k + 1][m + 1])
    r.append(l[0][0])
for i in range(len(r)):
    print(r[i])
