A, N, K = [int(i) for i in input().split()]
for i in range(K):
    print(A % (N + 1), end = ' ')
    A = int(A / (N + 1))