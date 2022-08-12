
def printN(n):
    if n==0:
        return
    ans = printN(n-1)
    print(n)
    return ans



n = int(input())
print(printN(n))