def sorted_list(arr):
    l = len(arr)
    if l==0 or l==1:
        return True
    if arr[0]>arr[1]:
        return False
    ans = sorted_list(arr[1:])
    if ans:
        return True
    else:
        return False



arr = [1,2,3,4,5,6]
print(sorted_list(arr))