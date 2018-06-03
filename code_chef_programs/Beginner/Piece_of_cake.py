for t in range(int(input())):
    s=input()
    c=[]
    d=tuple(s)
    for i in range(len(d)):
        c.append(s.count(d[i]))
    if max(c)==len(s)-max(c):
        print("YES")
    else:
        print("NO")