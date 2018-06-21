for t in range(int(input())):
    f=2
    s = [ch for ch in input()]
    l = len(s)
    s1 = s[:l//2]
    if l % 2 != 0:
        s2 = s[l//2+1:]
    else:
        s2 = s[l//2:]
    for i in range(l//2):
        if s1[i] in s2:
            s2.remove(s1[i])
        else:
            print("NO")
            f=1
            break
    if f==2:
        print("YES")