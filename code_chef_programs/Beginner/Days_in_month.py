for t in range(int(input())):
    w,s=[ch for ch in input().split()]
    L1=[4,4,4,4,4,4,4]
    L2=['mon','tues','wed','thurs','fri','sat','sun']
    if(int(w)==28):
        print(*L1,sep=' ')
    elif(int(w)==29):
        ind = L2.index(s)
        L1[ind] += 1
        print(*L1, sep=' ')
    elif (int(w)==30):
        ind = L2.index(s)
        L1[ind] += 1
        L1[(ind+1)%7] += 1
        print(*L1, sep=' ')
    else:
        ind = L2.index(s)
        L1[ind] += 1
        L1[(ind + 1)%7] += 1
        L1[(ind + 2)%7] += 1
        print(*L1, sep=' ')