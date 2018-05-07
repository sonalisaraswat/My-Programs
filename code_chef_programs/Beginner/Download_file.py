for tc in range(int(input())):
    c=0
    n, k=[int(j) for j in input().split()]
    d = k
    for i in range(n):
        t, da = [int(k) for k in input().split()]
        if k > 0:
            d = d - t
            if d<0:
                d=0
            t = t - k
            if t<0:
                t=0
            k = d
        c = c + (t * da)
    print(c)