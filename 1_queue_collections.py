# Implement a queue using collections module in Python.
from collections import deque


dq = deque([])
while True:
  ip = input("enter 1:insert,2:delete,3:view,4:exit\n")
  if ip == '1':
    x=input("enter a value\n")
    dq.append(x)
    print("inserted")
  elif ip == '2':
    if len(dq) == 0:
      print("queue is empty")
    else:
      dq.popleft()
      print("deleted")
  elif ip == '3':
    print(list(dq))
  else:
    break
    

