def issubstr(str):
    for j in range(K):
        if str.find(a[j]) != -1:
            return 1
    return 0
K, N = [int(i) for i in input().split()]
a=[]
for i in range(K):
    a.append(input())
for i in range(N):
    s = input()
    if len(s) >= 47:
        print("Good")
    else:
        ans = issubstr(s)
        if ans==1:
            print("Good")
        else:
            print("Bad")