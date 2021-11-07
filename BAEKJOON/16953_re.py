import sys
read=sys.stdin.readline

A,B=map(int,read().split())

ret=sys.maxsize-1

def recur(next,cnt):
    global ret
    if next==B:
        ret=min(ret,cnt)
        return
    if next>B:
        return
    recur(next*10+1,cnt+1)
    recur(next*2,cnt+1)
recur(A,1)
print(ret if ret<sys.maxsize-1 else -1)