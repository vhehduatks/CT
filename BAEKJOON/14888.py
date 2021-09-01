import sys
read=sys.stdin.readline

N=int(read())
Arr=list(map(int,read().split()))
Op=list(map(int,read().split()))
maxval=-sys.maxsize
minval=sys.maxsize-1


def bf(num,idx,op0,op1,op2,op3):
    global maxval,minval

    if len(Arr)==idx:
        maxval=max(maxval,num)
        minval=min(minval,num)
        return
    
    #이전의 op값들이 보존되어야 함 (완전탐색)
    if op0:
        bf(num+Arr[idx],idx+1,op0-1,op1,op2,op3)
    if op1:
        bf(num-Arr[idx],idx+1,op0,op1-1,op2,op3)
    if op2:
        bf(num*Arr[idx],idx+1,op0,op1,op2-1,op3)
    if op3:
        bf(int(num/Arr[idx]),idx+1,op0,op1,op2,op3-1)

bf(Arr[0],1,Op[0],Op[1],Op[2],Op[3])
print(maxval)
print(minval)