for t in range(int(input())):
    n = int(input())
    s = [ch for ch in input()]
    if 'I' in s:
        print("INDIAN")
    else:
        if 'Y' in s:
            print("NOT INDIAN")
        else:
            print("NOT SURE")