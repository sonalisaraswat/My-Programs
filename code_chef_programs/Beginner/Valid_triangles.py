for t in range(int(input())):
    a,b,c=[int(j) for j in input().split()]
    if a==0 or b==0 or c==0:
        print("NO")
    else:
        if(a+b+c==180):
            print("YES")
        else:
            print("NO")