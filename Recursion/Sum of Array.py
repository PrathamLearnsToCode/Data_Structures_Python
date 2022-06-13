def sum(arr,n):
   if len(arr) == 1:
       return arr[0]
   else:
    return arr[0] + sum(arr[1:],n)


arr = [1,2,3,4,5]
n = len(arr)
print(sum(arr,n))