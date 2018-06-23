while True:
    if input() == '0':
        break
    a=[int(i) for i in input().split()]
    flag=0
    for i in range(len(a)):
        j=a[i]
        if a[i]==j and a[j-1]!=i+1:
            flag=1
    if flag==0:
        print("ambiguous")
    else:
        print("not ambiguous")