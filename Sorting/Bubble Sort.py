def bubble_sort(list):
    l = len(list)
    for i in range(l):
        for j in range(0,l-1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1], list[j]



#Optimised
def bubble_SortOptimised(list):
    l = len(list)

    for i in range(l):
        swapped = False
        for j in range(l-i-1):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True

        if not swapped:
            break