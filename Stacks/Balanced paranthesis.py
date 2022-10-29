def isBalanced(string):
    stack = []
    for char in string:
        if char in '([{':
            stack.append(char)
        elif char is ')':
            if(not stack or stack[-1] !=)

