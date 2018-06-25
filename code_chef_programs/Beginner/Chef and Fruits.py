for t in range(int(input())):
    n, m, k = [int(i) for i in input().split()]
    diff = abs(n - m)
    if diff > 0:
        if diff <= k:
            print(0)
        else:
            print(diff-k)
    else:
        print(0)