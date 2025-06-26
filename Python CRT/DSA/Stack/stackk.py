
OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def infix_to_postfix(expression):
    stack = []
    output = []

    for ch in expression:
        if ch not in OPERATORS:     # Operand goes directly to output
            output.append(ch)

        elif ch == '(':        # Push '(' to stack
            stack.append(ch)

        elif ch == ')':         # Pop until '(' is found
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