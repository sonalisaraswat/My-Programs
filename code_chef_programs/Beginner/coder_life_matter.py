for t in range(int(input())):
    a=[int (j) for j in input().split()]
    one=0
    fin=1
    for i in range(30):
        if a[i]==1:
            one+=1
        if one>5:
            fin=2
            break
        if a[i]==0:
            one=0
    if fin==2:
        print("#coderlifematters")
    else:
        print("#allcodersarefun")
