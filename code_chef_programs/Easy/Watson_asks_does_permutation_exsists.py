for t in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    d = {int(j) for j in a}
    if (max(a)-min(a)+1) != len(d):
        print("NO")
    else:
        print("YES")