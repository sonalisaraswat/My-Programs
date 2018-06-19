def isnotPrime(n):
    if n%2==0:
        return 1
    else:
        for i in range(2,n):
            if n%i==0:
                return 1
        return 0
for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    c=a+b+1
    ans=1
    while(isnotPrime(c)==1):
        c+=1
        ans+=1
    print(ans)