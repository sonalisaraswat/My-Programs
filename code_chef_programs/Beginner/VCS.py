for t in range(int(input())):
    N,K,M=[int(j) for j in input().split()]
    a=[int(j) for j in input().split()]
    b=[int(j) for j in input().split()]
    s=set(a+b)
    print((len(a)+len(b)-len(s)),N-len(s))
