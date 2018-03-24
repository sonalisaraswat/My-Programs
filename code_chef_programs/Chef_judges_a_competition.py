for t in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    b = [int(i) for i in input().split()]
    s1 = sum(a)-max(a)
    s2 = sum(b)-max(b)
    if s2 < s1:
        print("Bob")
    elif s2 > s1:
        print("Alice")
    else:
        print("Draw")