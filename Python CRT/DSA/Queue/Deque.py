from collections import deque
dq=deque(['mon','tue','wed'])
print(dq)
dq.append('thu')
print(dq)
dq.appendleft('sun')
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)   
