def sum_array(arr):
    l = len(arr)
    if l == 0:
        return
    if l == 1:
        return arr[0]
    return arr[0] + sum_array(arr[1:])

arr = [1,2,3,4,5,6,7,8]
print(sum_array(arr))