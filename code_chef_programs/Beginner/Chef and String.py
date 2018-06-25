s = input()
c = h = e = f = 0
for i in range(len(s)):
    if s[i] == "C":
        c  += 1
    elif s[i] == "H" and h < c:
        h += 1
    elif s[i] == "E" and e < h:
        e += 1
    elif s[i] == "F" and f < e:
        f += 1
print(f)
