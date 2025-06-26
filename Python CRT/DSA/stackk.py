"""OPERATORS=set(['+','-','*','/','(',')','^'])
priority={'+':1,'-':1,'*':2,'/':2,'^':3}
def infix_to_postfix(expression):
    stack=[]
    output=''
    for ch in expression:
        if ch not in OPERATORS:
expression
        output+=ch
        elif ch=='(':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            #lesser priority cant be on top on hogher or equal priority
            #so pop and put in output
            while stack and stcak[-1]!='(' and PRIORITY[ch]
<=PRIORITY[stack[-1]]:
                output+=stcak.pop()
            stack.append(ch)

        while stcak:
            output+=stack.pop()
        return output
expression=input('enter infix expression')
print('infix expression:',expression)
print('postfix expression:',infix_to_postfix(expression))"""
OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def infix_to_postfix(expression):
    stack = []
    output = []

    for ch in expression:
        if ch not in OPERATORS:
            # Operand goes directly to output
            output.append(ch)

        elif ch == '(':
            # Push '(' to stack
            stack.append(ch)

        elif ch == ')':
            # Pop until '(' is found
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '(' from stack

        else:
            # Operator encountered
            while stack and stack[-1] != '(' and priority[ch] <= priority[stack[-1]]:
                output.append(stack.pop())
            stack.append(ch)

    # Pop any remaining operators
    while stack:
        output.append(stack.pop())

    return ''.join(output)

expression = input('Enter infix expression: ')
print('Infix expression:', expression)
print('Postfix expression:', infix_to_postfix(expression))