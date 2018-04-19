n=int(input())
c=[int(j) for j in input().split()]
w=[int(j) for j in input().split()]
mi=min(c)
mini=c.index(mi)
if w[mini]==3:
    print(mi)
elif w[mini]==1:
    t=[]
    for i in range(n):
        if w[i]==2:
            t.append(c[i])
    print(mi+min(t))
else:
    t = []
    for i in range(n):
        if w[i] == 1:
            t.append(c[i])
    print(mi + min(t))