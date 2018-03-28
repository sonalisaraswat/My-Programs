for t in range(int(input())):
    fro=0
    bac=0
    n=int(input())
    a = [int(j) for j in input().split()]
    g = [int(k) for k in input().split()]
    for i in range(n):
        if (g[i] < a[i]):
            fro = 1
            break
    g = g[::-1]
    for i in range(n):
        if g[i] < a[i]:
            bac = 1
            break
    if fro == 0 and bac == 0:
        print("both")
    elif fro == 0 and bac == 1:
        print("front")
    elif fro == 1 and bac == 0:
        print("back")
    else:
        print("none")

