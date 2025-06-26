'''1.scanning the expression from left to right
2.if scanned character is data item then appending to output,
if scanned character is operator,comparring the operator priority with the stack top most priority,
if operator priority scanned is higher than the stack top most operator priority pushing onto the stack,
other wise pop the stack top most  operator and then push the scanned ooperator
3.If the scanned character is ')' pop all the items from the stack till'('''

def isBalanced(s):
    stack=[]
    bracketDict={
        "}":"{",
        "]":"[",
        ")":"(",
    }
    for b in s:
        if b in bracketDict and stack and bracketDict[b]==stack[-1]:
            stack.pop()
        else:
            stack.append(b)
    if stack:
        return("NO")
    else:
        return("YES")
s="{}"
ans=isBalanced(s)
print(ans)