def isValid(s):
        d={")":"(","}":"{","]":"["}
        stack=[]
        if len(s)==1:
            return False
        for i in s:
            if i=="(" or i=="{" or i=="[":
                stack.append(i)
            elif(not stack):
                return False
            else:
                if d[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
s = "()[]{}"
print(isValid(s))