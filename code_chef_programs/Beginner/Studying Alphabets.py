s = [ch for ch in input()]
for n in range(int(input())):
    w = input()
    f=1
    for i in range(len(w)):
        if w[i] not in s:
            print("No")
            f=2
            break
    if f == 1:
        print("Yes")