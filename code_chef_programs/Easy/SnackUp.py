for t in range(int(input())):
    nj=int(input())
    print(nj)
    a=[(i%nj)+1 for i in range(nj)]
    for j in range(nj):
        print(nj)
        c=j
        for k in range(nj):
            print((k + 1), a[c%nj], a[(c + 1)%nj])
            c+=1