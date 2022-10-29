def reverseStack(s1,s2):
    if(len(s1) <=1):
        return
    while(len(s1) != 1):
        x = s1.pop()
        s2.append(x)

    while(len(s2) != 0):
        x = s2.pop()
        s1.append(x)


