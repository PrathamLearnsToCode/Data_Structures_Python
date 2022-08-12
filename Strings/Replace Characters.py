# Replace a with e
def ReplaceChar(string,char1,char2):
    newStr = ""
    for char in string:
        if(char==char1):
            newStr = char2 + newStr
        else:
            newStr = char + newStr

    return newStr

str = "abcdbtajea"
str = ReplaceChar(str,'a','e')
print(str)
