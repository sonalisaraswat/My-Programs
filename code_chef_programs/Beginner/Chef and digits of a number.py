for t in range(int(input())):
    s=[int(ch) for ch in input()]
    if len(s)==1:
        print("Yes")
    else:
        if s.count(1) == 1 or s.count(0) == 1:
            print("Yes")
        else:
            print("No")
