x = int(input())
def CheckNumber(n):
    if len(n) == 0:
        return False
    if n[0] == x:
        return True

    return CheckNumber(n[1:])

n = [1,2,3,4,5,6]
print(CheckNumber(n))

