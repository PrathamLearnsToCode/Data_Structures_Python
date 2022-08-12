def ReplacePi(string,x):
    l = len(string)
    if l<2:
        return string
    if string[0] == "p" and string[1] == "i":
        return x + ReplacePi(string[1:],x)
    return string[0] + ReplacePi(string[1:],x)

print(ReplacePi("pindjspfbdpidncpi","3.14"))



