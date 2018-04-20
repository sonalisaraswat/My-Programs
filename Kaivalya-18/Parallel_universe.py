n, m=[int(j) for j in input().split()]
s=[]
ans=[]
for i in range(n):
    s.append(input())
ans.append(s[n-1].count("A"))
while(n>1):
    co=n-1
    fs=s[co]
    ss=s[co-1]
    ns=''
    al=0
    for j in range(m):
        if fs[j]!=ss[j]:
            al+=1
            ns=ns+"A"
        else:
            ns=ns+"D"
    s[co-1]=ns
    ans.append(al)
    n-=1
qwer=ans[::-1]
print(*qwer, sep=" ")