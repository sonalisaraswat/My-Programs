for t in range(int(input())):
    n=int(input())
    c=0
    a=[(2**i) for i in range(12)]
    if n in a:
        print(1)
    else:
        for i in range(11,0,-1):
            if n>a[i] and n not in a :
                while(n>a[i]):
                    n=n-a[i]
                    c+=1
            if n in a:
                n=0
                c+=1
            if n==0:
                break
        print(c)