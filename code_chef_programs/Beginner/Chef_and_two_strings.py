for t in range(int(input())):
    a=input()
    b=input()
    p = maxd = 0
    for i in range(len(a)):
        if a[i]=='?' or b[i]=='?':
            p+=1
            maxd+=1
        elif (a[i]!=b[i]) and a[i]!='?' and b[i]!='?':
            maxd += 1
    print(abs(p-maxd),maxd)
