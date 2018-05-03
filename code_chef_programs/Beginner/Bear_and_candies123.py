for t in range(int(input())):
    a, b=[int(j) for j in input().split()]
    le = int(a**(1/2))
    be = (le*le)+le
    if b >= be:
        print("Bob")
    else:
        print("Limak")