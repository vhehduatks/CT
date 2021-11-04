import sys
read=sys.stdin.readline

N=int(read())
intarr=[int(read()) for _ in range(N)]
maxnum=N
sortedlen=0
for i in reversed(intarr):
    if i==maxnum:
        maxnum-=1
        sortedlen+=1
print(N-sortedlen)
