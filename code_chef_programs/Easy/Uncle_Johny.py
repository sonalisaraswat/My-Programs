for t in range(int(input())):
    n=input()
    li=[int(i) for i in input().split()]
    k=int(input())
    n=li[k-1]
    li.sort()
    print(li.index(n)+1)

