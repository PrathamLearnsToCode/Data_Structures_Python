def linear_search(data,item):
    for i in range(len(data)):
        if data[i] == item:
            return i
        return -1
