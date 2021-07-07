import sys

read=sys.stdin.readline

N,B=map(int,read().split())

def recur(N,B):
    ret=''
    if N==0:
        # if N:
            # ret=str(N)
        return ret
    new_N=N//B
    temp=N%B
    if temp>10:
        ret=chr(65+temp-10)
    else:
        ret=str(temp)
    return recur(new_N,B)+ret


print(recur(N,B))
