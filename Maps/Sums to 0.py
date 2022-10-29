arr = [-2,2,3,6,-6,2,-2]
d = {}

for words in arr:
    if words in d:
        d[words] = d[words] + 1
    else:
        d[words] = 1

