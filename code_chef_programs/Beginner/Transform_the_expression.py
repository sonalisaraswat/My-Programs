for t in range(int(input())):
    s=input()
    pre=['+','-','*','/','^']
    a=[]
    st=[]
    for i in range(len(s)):
        if ord(s[i]) in range(97,123):
            a.append(s[i])
        elif s[i]=="(":
            st.append("(")
        elif s[i]==")":
            while(st[len(st)-1]!="("):
                a.append(st.pop())
            st.pop()
        else:
            if s[i]=='*' or s[i]=='/' or s[i]=='^':
                st.append(s[i])
            elif st[len(st)-1]=="(" or st[len(st)-1]=="-" or st[len(st)-1]=="+":
                st.append(s[i])
            else :
                while st[len(st)-1]=="*" or st[len(st)-1]=="/" or st[len(st)-1]=="^" or st[len(st)-1]=="(":
                    a.append(st.pop())
                st.append(s[i])
    print("".join(a))
