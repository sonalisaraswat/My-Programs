for t in range(int(input())):
    d, n = [int(j) for j in input().split()]
    for i in range(d):
        n =int((n*(n+1))/2)
    print(n)

