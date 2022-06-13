n = int(input())
def numbers(n):
    if n==0:
        return 0
    print(n)
    numbers(n-1)



print(numbers(10))