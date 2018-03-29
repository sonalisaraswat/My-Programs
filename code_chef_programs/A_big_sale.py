for t in range(int(input())):
    loss=0
    for n in range(int(input())):
        p1=0
        p2=0
        p,q,d=[int(j) for j in (input().split())]
        p1=p+(d*p/100)
        p2=p1-(d*p1/100)
        loss =loss + (p-p2)*q
    print(loss)
