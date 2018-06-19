for n in range(int(input())):
    s=input()
    c=0
    a=[]
    for i in range(len(s)-3):
        if s[i]=='c' or s[i]=='h' or s[i]=='e' or s[i]=='f':
            a=[s[i],s[i+1],s[i+2],s[i+3]]
            if ('c' in a) and ('h' in a) and ('e' in a) and ('f' in a):
                c+=1
    if c>0:
        print("lovely",c)
    else:
        print("normal")
