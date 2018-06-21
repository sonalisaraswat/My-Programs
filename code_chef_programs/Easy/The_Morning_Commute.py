for test in range(int(input())):
    time=0
    for n in range(int(input())):
        x, t, f = [int(i) for i in input().split()]
        if x>=time:
            time+=(x-time)
        if (time-x)%f != 0:
            time += (f-(time-x)%f + t)
        else:
            time += t
    print(time)