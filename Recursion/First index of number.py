def first_occurence(arr,n):
    l = len(arr)
    if l==0:
        return -1
    if n not in arr:
        return -1
    if arr[0] == n:
        return 0
    ans = first_occurence(arr[1:], n)
    return ans

arr = [1,2,3,6,8,3,7,8]
n = 8
print(first_occurence(arr,n))