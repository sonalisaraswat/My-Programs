for t in range(int(input())):
    s=input()
    l=len(s)
    a=['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ins = 2
    for i in range(1,l):
        i1 =  a.index(s[i-1])
        i2 = a.index(s[i])
        if i2 > i1:
            ins += (i2 - i1) + 1
        elif i2 < i1:
            ins += (26-(i1+1)) + (i2 + 1) + 1
        else:
            ins+=1
    if ins > 11*l:
        print("NO")
    else:
        print("YES")