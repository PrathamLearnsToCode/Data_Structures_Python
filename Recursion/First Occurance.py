x = int(input())
def FirstOccurance(n):
    if len(n) == 0:
        return -1
    #if not n[0] == x:
        return -1
    if n[0] == x:
        return 0

    return FirstOccurance(n[1:])

n = [1,2,3,4,5,6,7,8,9]
print(FirstOccurance(n))
