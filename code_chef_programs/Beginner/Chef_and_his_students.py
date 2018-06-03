for t in range(int(input())):
    s=input()
    p=0
    for i in range(len(s)-1):
        if(s[i]=="<" and s[i+1]==">"):
            p+=1
    print(p)