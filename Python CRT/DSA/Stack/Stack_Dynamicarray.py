a_stack =stack()
while True:
    print('push <value>')
    print('pop')
    print('display')
    print('quit')
    do=input('What would you like to do?').split()

    operation =do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty. ')
        else:
            print('Popped value: ',int(popped))
    elif operation=="display":
        a_stack.display()
    elif operation== 'quit':
        break