f = 0
for t in range(int(input())):
    c = 0
    s = input()
    for i in range(len(s)-1):
        if s[i] == "c" and s[i+1] == "h":
            c += 1
            break
        elif s[i] == "h" and s[i+1] == "e":
            c += 1
            break
        elif s[i] == "e" and s[i+1] == "f":
            c += 1
            break
    if c >= 1:
        f += 1
print(f)