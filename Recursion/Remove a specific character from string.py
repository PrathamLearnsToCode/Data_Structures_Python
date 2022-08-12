'''
Given a string, compute recursively a new string
where all 'x' chars have been removed.
'''
def removeChar(string,n):
    l= len(string)
    if l == 0:
        return string
    ans = removeChar(string[1:],n)
    if string[0] == n:
        return ans
    return string[0] + ans

print(removeChar("abcxxxcdxd","x"))