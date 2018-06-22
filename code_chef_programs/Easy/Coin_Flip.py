for t in range(int(input())):
    for g in range(int(input())):
        I, N, Q = [int(i) for i in input().split()]
        if N % 2 == 0:
            print(int(N/2))
        else:
            if I == Q:
                print(int(N/2))
            else:
                print(int(N/2)+1)