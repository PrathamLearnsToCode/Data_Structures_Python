def BinarySearch(data,item):
    lower = 0
    high = len(data)
    while lower<=high:
        middle = (lower + high) // 2
        if data[middle] == item:
            return middle
        elif data[middle] > item:
            high = middle - 1
        else:
            lower = middle + 1
    return -1

data = [1,2,3,4,5,6,7]
item = 6
print(BinarySearch(data,item))

# Recursive

def BinarySearchRecursive(data,low,high,item):
    while low<=high:
        middle = (low + high) // 2
        if data[middle] == item:
            return middle
        elif data[middle] > item:
            return BinarySearchRecursive(data, low, middle-1, item)
        else:
            return BinarySearchRecursive(data, middle+1, high, item)
    return -1

data = [1,2,3,4,5,6,7]
item = 7
print(BinarySearchRecursive(data,0,len(data),item))
