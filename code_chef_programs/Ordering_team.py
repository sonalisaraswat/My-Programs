for t in range(int(input())):
    ac=0
    bc=0
    cc=0
    f=0
    a=[int(n) for n in input().split()]
    b=[int(j) for j in input().split()]
    c=[int(k) for k in input().split()]
    for i in range(3):
        if a[i]>=c[i]:
            ac+=1
        if c[i]>=a[i]:
            cc+=1
    if ac==3 and sum(a)>sum(c):
        f+=1
    elif cc==3 and sum(c)>sum(a):
        f+=1
    else:
        print("no")
    ac=0
    cc=0
    i=0
    if f==1:
        while i < 3:
            if a[i] >= b[i]:
                ac += 1
            if b[i] >= a[i]:
                bc += 1
            i += 1
        if ac == 3 and sum(a) > sum(b):
            f += 1
        elif bc == 3 and sum(b) > sum(a):
            f += 1
        else:
            print("no")
    bc = 0
    ac = 0
    i = 0
    if f==2:
        while i < 3:
            if b[i] >= c[i]:
                bc += 1
            if c[i] >= b[i]:
                cc += 1
            i += 1
        if bc == 3 and sum(b) > sum(c):
            f += 1
        elif cc == 3 and sum(c) > sum(b):
            f += 1
        else:
            print("no")
    if f==3:
        print("yes")