x = int(input())
n = int(input())
def power(x,n):
    if n==0:
        return 1

    return (x)*(x**(n-1))

print(power(2,3))
