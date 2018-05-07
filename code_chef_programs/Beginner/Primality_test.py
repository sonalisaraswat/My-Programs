for t in range(int(input())):
    n=int(input())
    f=0
    for i in range(2,n,1):
        if n%i==0:
            print("no")
            f=1
            break
    if f==0:
        print("yes")