for t in range(int(input())):
    te = int(input())
    if te>0:
        s1 = input()
        c1 = 1
        c2 = 0
        if te-1>0:
            for i in range(te - 1):
                ss = input()
                if (ss == s1):
                    c1 += 1
                else:
                    s2 = ss
                    c2 += 1
            if c1 > c2:
                print(s1)
            elif c2 > c1:
                print(s2)
            else:
                print('Draw')
        else:
            print(s1)
    else:
        print("Draw")