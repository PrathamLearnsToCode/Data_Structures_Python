'''
Write a program to find x to the power n (i.e. x^n). Take x and n from the user.
'''

def power(x,n):
    if x==0:
        return
    return (x**-1)*(x**(n+1))


x = int(input())
n = int(input())
print(power(x,n))
