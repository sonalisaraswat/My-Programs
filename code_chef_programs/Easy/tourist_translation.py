t,d=[ch for ch in input().split()]
d1 = [ch.lower() for ch in d]
d2 = [chh.upper() for chh in d1]
for _ in range(int(t)):
    s=input()
    a = []
    for i in range(len(s)):
       if ord(s[i]) in range(65,91):
           a.append(d2[ord(s[i])-65])
       elif ord(s[i]) in range(97,124):
           a.append(d1[ord(s[i])-97])
       elif s[i]=='_':
            a.append(" ")
       else:
           a.append(s[i])
    print(''.join(a))