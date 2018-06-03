def fun(s):
    bal=0
    maxbal=0
    for i in range(len(s)):
        if s[i]=='(':
            bal+=1
        else:
            bal-=1
        maxbal=max(maxbal,bal)
    return maxbal
for t in range(int(input())):
    s=input()
    ab=''
    m=fun(s)
    for i in range(m):
        ab=ab+"("
    for j in range(m):
        ab=ab+")"
    print(ab)