for t in range(int(input())):
    h, m = [int(j) for j in input().split()]
    h-=1
    m-=1
    if h==10:
        h-=1
    if m==10:
        m-=1
    if h<10 and m<10:
        print(min(h,m)+1)
    else:
        if h>10 and m>10:
            h=h-(h%11)
            m=m-(m%11)
            print(2* (min(h//10, m//10)) + 10 + max(h//10, m//10))
        elif h>10 and m<10:
            h=h-(h%11)
            print(1 + m + (min(h//10, m)))
        else:
            m=m-(m%11)
            print(1 + h + (min(h, m//10)))