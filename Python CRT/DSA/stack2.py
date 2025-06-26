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