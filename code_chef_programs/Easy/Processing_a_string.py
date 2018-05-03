for t in range(int(input())):
    s=[ord(ch) for ch in input()]
    sum=0
    for i in range(len(s)):
        if s[i] >= 49 and s[i]<=57:
            sum=sum+int(s[i])-48
    print(sum)