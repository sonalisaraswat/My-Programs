for t in range(int(input())):
    f1 = f2 = f3 = 0
    h, c, T = [j for j in input().split()]
    if int(h) > 50:
        f1 = 1
    if float(c) < 0.7:
        f2 = 1
    if int(T) > 5600:
        f3 = 1
    if f1 == f2 == f3 == 1:
        print(10)
    elif f1 == 1 and f2 == 1 and f3 == 0:
        print(9)
    elif f2 == 1 and f3 == 1 and f1 == 0:
        print(8)
    elif f1 == 1 and f3 == 1 and f2 == 0:
        print(7)
    elif (f1 == 1 and f2 ==0 and f3 == 0) or (f2 == 1 and f1 == 0 and f3 == 0) or (f3==1 and f1==0 and f2==0):
        print(6)
    elif f1 == f2 == f3 == 0:
        print(5)
