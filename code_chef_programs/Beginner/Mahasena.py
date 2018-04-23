t=int(input())
even=odd=0
a=[int(j) for j in input().split()]
for i in range(t):
    if a[i]%2==0:
            even+=1
    else:
            odd+=1
if even>odd:
        print("READY FOR BATTLE")
else:
        print("NOT READY")