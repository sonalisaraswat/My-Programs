def fun(x,y,s,a):
    x=str(x)
    if x in s:
        for i in range(y,10):
            if(str(i) in s):
                if x==str(i):
                    if s.count(x)>=2:
                        a.append(chr(int(x+str(i))))
                else:
                    a.append(chr(int(x+str(i))))
    return a
for t in range(int(input())):
    s=input()
    a=[]
    a=fun(6,5,s,a)
    a=fun(7,0,s,a)
    a=fun(8,0,s,a)
    if('9' in s) and ('0' in s):
        a.append('Z')
    a=''.join(a)
    print(a)




