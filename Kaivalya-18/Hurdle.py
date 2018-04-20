for t in range(int(input())):
    N, H, U, E=[int(j) for j in input().split()]
    h=[int(j) for j in input().split()]
    if H<max(h):
        print(-1)
    else:
        U=U-(sum(h)*E)
        if U>0:
            U=U//E
            print(U)
        elif U<0:
            print(-1)
        else:
            print(0)
