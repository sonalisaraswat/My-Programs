for t in range(int(input())):
    s=input()
    tran = 0
    if s[0] != s[7]:
        tran += 1
    for i in range(7):
        if s[i]!=s[i+1]:
            tran += 1
    if tran >2:
        print("non-uniform")
    else:
        print("uniform")