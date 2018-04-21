for t in range(int(input())):
    n, k = [int(j) for j in input().split()]
    s = [int(j) for j in input().split()]
    ar = [0 for x in range(200001)]
    for i in s:
        ar[i] = 1
    if k == 0:
        for i in range(len(ar)):
            if ar[i] == 0:
                print(i)
                break
    else:
        for i in range(len(ar)):
            if ar[i] == 0 and k > 0:
                k -= 1
            elif ar[i] != 1:
                print(i)
                break