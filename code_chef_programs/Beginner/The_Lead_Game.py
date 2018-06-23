a = b = le = 0
for t in range(int(input())):
    x, y = [int(i) for i in input().split()]
    a += x
    b += y
    if abs(a-b)>le:
       le = abs(a-b)
       if a>b:
           play=1
       else:
           play=2
print(play,le)