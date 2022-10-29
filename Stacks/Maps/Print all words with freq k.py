s = "this is a word string containing many many words"
k = 2

words = s.split()
d = {}
for w in words:
    if w in d:
        d[w] = d[w] + 1

    else:
        d[w] = 1

print(d)

'''
Alternate
'''

s = "this is a word string containing many many words"
k = 2

words = s.split()
d = {}
for w in words:
    if w in d:
        d[w] = d.get(w,0) + 1

    else:
        d[w] = 1

print(d)


