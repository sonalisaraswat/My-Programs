for t in range(int(input())):
    a=[ch for ch in input()]
    b=input()
    f=2
    for i in range(len(b)):
        if b[i] in a:
            f=1
            print("Yes")
            break
    if f==2:
        print("No")