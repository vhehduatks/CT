import sys
read=sys.stdin.readline

Arr=list(read().strip())
Stack=[]

try:
    Stack.append(Arr.pop(0))
    while Arr:
        temp=Arr.pop(0)
        if isinstance(Stack[-1],str) and Stack[-1]+temp=='()':
            Stack.pop()
            Stack.append(2)
        elif isinstance(Stack[-1],str) and Stack[-1]+temp=='[]':
            Stack.pop()
            Stack.append(3)
        elif temp==')':
            temp_num=0
            while 1:
                if Stack[-1]=='(':
                    break
                temp_num+=Stack.pop()
            Stack.pop()
            Stack.append(temp_num*2)
        elif temp==']':
            temp_num=0
            while 1:
                if Stack[-1]=='[':
                    break
                temp_num+=Stack.pop()
            Stack.pop()
            Stack.append(temp_num*3)
        else:
            Stack.append(temp)


    print(sum(Stack))
except Exception as e:
    print(0)
  
    