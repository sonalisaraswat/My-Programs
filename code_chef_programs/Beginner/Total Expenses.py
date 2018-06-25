for t in range(int(input())):
    q, p = [float(i) for i in input().split()]
    if q > 1000:
        p = p * q
        p = p - (0.1 * p)
    else:
        p = p * q
    print('%0.6f'%(p))