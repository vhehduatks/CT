import sys
read=sys.stdin.readline
sys.setrecursionlimit(9000)
N,S=map(int,read().split())
Arr=list(map(int,read().split()))
count=sys.maxsize-1

def recur(nextarr):
    global count
    if not nextarr:
        return
    Sum=0
    for i,a in enumerate(nextarr,start=1):
        Sum+=a
        if Sum>=S:
            count=min(count,i)
            break

    nextarr.pop(0)
    recur(nextarr)

if sum(Arr)<S:
    print(0)
else:
    recur(Arr)  
    print(count)