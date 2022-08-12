def removeDuplicates(string):
    l = len(string)
    if l < 2:
        return string
    ans = removeDuplicates(string[1:])
    if string[0] != string[1]:
        return string[0] + ans
    return  ans

print(removeDuplicates("aaabbbccddde"))