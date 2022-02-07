import sys
read=sys.stdin.readline

T=int(read())

zero_cnt=0
one_cnt=0

def fibo(N):
    global zero_cnt
    global one_cnt
    if N==0:
        zero_cnt+=1
        return 0
    elif N==1:
        one_cnt+=1
        return 1
    else:
        return fibo(N-1)+fibo(N-2)
        

for _ in range(T):
    n=int(read())
    fibo(n)
    print(zero_cnt,one_cnt)
    zero_cnt=0
    one_cnt=0