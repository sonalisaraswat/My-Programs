for t in range(int(input())):
    s,sg,fg,d,T=map(int,input().split())
    ans=s+((d*180)/T)
    if abs(ans-sg)<abs(ans-fg):
        print("SEBI")
    elif abs(ans-sg)>abs(ans-fg):
        print("FATHER")
    else:
        print("DRAW")