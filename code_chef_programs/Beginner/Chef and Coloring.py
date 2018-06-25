for t in range(int(input())):
    n = int(input())
    s=[(ch) for ch in input()]
    c=max(s.count('R'), s.count('G'), s.count('B'))
    print(n-c)
