def isSorted(n):
    l = len(n)
    if l==0 or l==1:
        return True

    if n[0]> n[1]:
        return False
    smallerList = n[1: ]
    isSmallerListSorted = isSorted(smallerList)
    if isSmallerListSorted:
        return True
    else:
        return False

n = [1,2,6,4,5,7]
print(isSorted(n))