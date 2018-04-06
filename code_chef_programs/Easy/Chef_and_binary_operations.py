for t in range(int(input())):
    a=[int(j) for j in input()]
    b=[int(j) for j in input()]
    x = y = c =0
    if 0 in a and 1 in a:
        for i in range(len(a)):
            if a[i] != b[i]:
                if a[i] == 1:
                    x += 1
                else:
                    y += 1
        while x > 0 and y > 0:
            c += 1
            x -= 1
            y -= 1
        if x > 0:
            c += x
        if y > 0:
            c += y
        print("Lucky Chef")
        print(c)
    else:
        print("Unlucky Chef")
