import sys
read=sys.stdin.readline

A,B=map(int,read().split())

def recur(A,ret):
    if A>B:
        return 9999
    if A==B:
        return ret
    
    return min(recur(A*2,ret+1),recur(int(str(A)+"1"),ret+1))

ret=recur(A,1)
print(ret if ret!=9999 else -1)