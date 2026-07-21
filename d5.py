# Given a string containing only:
# ( ) { } [ ]
# Return:
# True → if every opening bracket has the correct closing bracket.
# False → otherwise.

def isvalid(s):
    stack=[]
    mapping = { ']':'[' , ')':'(' , '}':'{' }
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0


strr=input("enter expression containing only ( ) { } [ ] :  ")
print(isvalid(strr))