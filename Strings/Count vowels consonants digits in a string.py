'''
Given a string, write a program to count the
number of vowels, consonants, and spaces in that string.
'''


def countInstring(str):
    v,c,d,s = 0,0,0,0
    for i in str:
        if ((i>='a' and i<='z') or (i>='A' and i<='Z')):
            i = i.lower()
            if(i == 'a' or i=='e' or i =='i' or i =='o' or i=='u'):
                v = v + 1
            else:
                c = c + 1
        elif(i>='0' and i<='9'):
            d = d+1
        else:
            s = s+1
    return v,c,d,s

str = 'aeioug375hjdf cnjv@!'
#type(str[0])
v,c,d,s = countInstring(str)
print(v,c,d,s)