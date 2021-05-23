import sys
read=sys.stdin.readline

stack1=list(read()[:-1])
stack2=list()
M=int(read())

for _ in range(M):
    command=read()[:-1].split()

    if command[0]=='L': 
        if stack1:
            stack2.append(stack1.pop())
    elif command[0]=='D':
        if stack2:
            stack1.append(stack2.pop())
    elif command[0] =='B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(command[1])
while stack2:
    stack1.append(stack2.pop())
print(''.join(stack1))

