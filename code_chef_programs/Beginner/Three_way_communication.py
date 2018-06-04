for t in range(int(input())):
    r=int(input())
    c=0
    x1, y1 = [int(i) for i in input().split()]
    x2, y2 = [int(i) for i in input().split()]
    x3, y3 = [int(i) for i in input().split()]
    d12 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    d13 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    d23 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    if(d12<=r):
        c+=1
    if(d23<=r):
        c+=1
    if(d13<=r):
        c+=1
    if c>=2:
        print("yes")
    else:
        print("no")