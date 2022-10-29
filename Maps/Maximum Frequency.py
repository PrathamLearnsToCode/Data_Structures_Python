arr = [13,8,5,6,3,6,7,6]
d = {}
for int in arr:
    if int in d:
        d[int] = d[int] + 1
    else:
        d[int] = 1

print(d)

for key,values in d.items():
    print(f"key:{key},values:{values}")

maxkey = max(d, key = d.get('6'))
print(maxkey)

