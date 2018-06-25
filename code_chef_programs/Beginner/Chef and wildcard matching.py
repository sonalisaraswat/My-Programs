for t in range(int(input())):
    f = 0
    x = [ch for ch in input()]
    y = [ch for ch in input()]
    for i in range(len(x)):
        if x[i] == y[i] or (x[i] != "?" and y[i] == "?") or (x[i] == "?" and y[i] != "?"):
            f += 1
        else:
            print("No")
            break
    if f == len(x):
        print("Yes")