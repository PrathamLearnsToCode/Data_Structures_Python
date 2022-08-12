def check_number(arr,n):
    l = len(arr)
    if l==0:
        return False
    if arr[0] == n:
        return True
    ans = check_number(arr[1:],n)
    if ans:
        return True
    else:
        return False


n = int(input())
arr = [1,2,3,4,5,6,7]
print(check_number(arr,n))