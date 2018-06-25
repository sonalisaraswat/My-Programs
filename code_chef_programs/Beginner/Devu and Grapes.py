for t in range(int(input())):
    n, k =[int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    q = 0
    for i in range(n):
        if a[i]<k:
            inc = ((a[i] // k + 1) * k) - a[i]
            q += inc
        else:
            re = a[i] % k
            inc = ((a[i]//k+1)*k)- a[i]
            if re>inc:
                q += inc
            else:
                q += re
    print(q)