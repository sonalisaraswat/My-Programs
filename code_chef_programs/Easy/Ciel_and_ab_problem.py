a, b=[int(j) for j in input().split()]
ans=a-b
if ans%10==1:
    print(int(ans/10)*10+2)
else:
   print(int(ans/10)*10+1)
