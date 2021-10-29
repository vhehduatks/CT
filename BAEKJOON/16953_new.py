import sys
read=sys.stdin.readline

A,B=map(int,read().split())

minval=sys.maxsize-1
def dfs(A,cnt):
    global minval
    if A>B:
        return
    if  A==B:
        minval=min(minval,cnt)

    dfs(A*2,cnt+1)
    dfs(A*10+1,cnt+1)
   
dfs(A,1)

print(minval if minval<(sys.maxsize-1) else -1)