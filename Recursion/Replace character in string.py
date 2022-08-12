def ReplaceChar(string,a,b):
    l = len(string)
    if l == 0:
        return string
    ans = ReplaceChar(string[1:],a,b)
    if string[0] == a:
        return b + ans
    else:
        return string[0] + ans

print(ReplaceChar("yoloxxx","x","69"))