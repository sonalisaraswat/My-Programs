for t in range(int(input())):
    a, b=[int(j) for j in input().split()]
    if abs(a-b)==2:
        print("YES")
    elif min(a,b)%2==1 and abs(a-b)==1:
        print("YES")
    else:
        print("NO")