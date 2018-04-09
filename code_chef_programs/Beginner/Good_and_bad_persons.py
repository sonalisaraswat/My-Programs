for t in range(int(input())):
    n, k = [int(h) for h in input().split()]
    s = input()
    u = l =0
    for i in range(n):
        if s[i].isupper():
            u += 1
        elif s[i].islower():
            l += 1
    if u<=k and l<=k:
        print("both")
    elif u<=k and l>k:
        print("chef")
    elif u>k and l<=k:
        print("brother")
    elif u>k and l>k:
        print("none")