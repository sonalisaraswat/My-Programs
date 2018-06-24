for t in range(int(input())):
    n, k = [int(i) for i in input().split()]
    max = 0
    for i in range(1,k+1):
        if n % i > max:
            max = n % i
    print(max)