'''
For a given a string(str), find and
return the highest occurring character.
'''
def highOccur(str):
    d = {}
    for i in str:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    keymax = max(d,key = d.get)
    return keymax



str = 'fjwiedbbajrbafbsifbo'
updated = highOccur(str)
print(updated)