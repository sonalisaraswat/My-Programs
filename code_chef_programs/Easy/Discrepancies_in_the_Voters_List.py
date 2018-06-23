from sys import stdin,stdout
a, b, c = [int(x) for x in stdin.readline().split()]
d = {}
for i in range(a + b + c):
	x = int(input())
	if x not in d:
		d[x] = 0
	d[x] += 1
ans = []
for x in d:
	if d[x] > 1:
		ans.append(x)
ans.sort()
print(len(ans))
for a in ans:
	print(a)