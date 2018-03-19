for t in range(int(input())):
    s=input()
    if s.count('1')==0:
        print("Beginner")
    elif s.count('1')==1:
        print("Junior Developer")
    elif s.count('1')==2:
        print("Middle Developer")
    elif s.count('1')==3:
        print("Senior Developer")
    elif s.count('1')==4:
        print("Hacker")
    else:
        print("Jeff Dean")