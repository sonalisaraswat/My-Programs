for t in range(int(input())):
    f=0
    n=[int(j) for j in input()]
    a = n[int((len(n) + 1) / 2):]
    n = n[0:int(len(n) / 2)]
    a = a[::-1]
    for i in range(len(a)):
        if n[i]!=a[i]:
            print("losses")
            f=1
            break
    if f==0:
        print("wins")