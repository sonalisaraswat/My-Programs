for t in range(int(input())):
    n = int(input())
    ans = 0
    if n >= 100:
        ans = ans + (n//100)
        n=n%100
    if n >= 50:
        ans = ans + (n//50)
        n=n%50
    if n >= 10:
        ans = ans + (n//10)
        n=n%10
    if n >= 5:
        ans = ans + (n // 5)
        n = n % 5
    if n >= 2:
        ans = ans + (n//2)
        n=n%2
    if n == 1:
        ans = ans + 1
    print(ans)