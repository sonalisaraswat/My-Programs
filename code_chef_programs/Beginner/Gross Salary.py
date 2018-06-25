for t in range(int(input())):
    sal = int(input())
    if sal < 1500:
        sal = sal + (0.1 * sal) + (0.9 * sal)
    else:
        sal = sal + 500 + (0.98 * sal)
    print(sal)