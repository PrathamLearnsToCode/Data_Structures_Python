'''
For a given a string(str) and a character X,
write a function to remove all the occurrences of X
from the given string.
The input string will remain unchanged if the given character(X)
doesn't exist in the input string.
'''

def removeChar(string,x):
    newStr = ''
    for i in range(len(string)):
        if string[i] != x:
            newStr = string[i] + newStr
    return newStr





string = 'abdhaabfja'
x = 'a'
str = removeChar(string,x)
print(str)