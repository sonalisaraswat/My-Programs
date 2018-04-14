for t in range(int(input())):
    s=[ch for ch in input().split()]
    a=[int(j) for j in input().split()]
    even = odd = 0
    if int(s[0])==1 and s[1]=="Dee" and a[0]%2==0:
        print("Dee")
    else:
        print("Dum")