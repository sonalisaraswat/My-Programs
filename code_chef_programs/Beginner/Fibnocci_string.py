for t in range(int(input())):
    s=input()
    se=set(s)
    a=list(se)
    l=len(a)
    if l<3:
        print("Dynamic")
    else:
        for i in range(l):
            a[i]=s.count(a[i])
        a.sort()
        f=1
        if len(a) > 3 and a[3] != a[2] + a[1]:
            a[0], a[1] = a[1], a[0]
        for i in range(2,l):
            if a[i] != a[i-1] + a[i-2]:
                print("Not")
                f=2
                break
        if f==1:
            print("Dynamic")
