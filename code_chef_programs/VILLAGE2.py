for t in range(int(input())):
    s = input()
    i = a = b = d = 0
    while i < (len(s)):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += 1
        elif s[i] == '.' and i == 0:
            while s[i] != '.' and i < len(s):
                i += 1
        elif s[i] == '.':
            ch = s[i-1]
            while i < len(s)-1 and s[i] == '.':
                d += 1
                i += 1
            if s[i] == ch:
                if ch == 'A':
                    a += (d + 1)
                    d = 0
                elif ch == 'B':
                    b += (d + 1)
                    d = 0
            else:
                if s[i] == 'A':
                    a += 1
                elif s[i] == 'B':
                    b += 1
                d = 0
        i += 1
    print(a,b)