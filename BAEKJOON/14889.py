import sys
read=sys.stdin.readline

N=int(read())

matrix=[]

for _ in range(N):
    temp=list(map(int,read().split()))
    matrix.append(temp)

visit=[False]*N
minval=sys.maxsize-1

def back_track(idx,depth):
    global minval
    global visit
    if depth==N//2:
        start=0; link=0
        for i in range(N):
            for j in range(i,N):
                if visit[i] and visit[j]:
                    start += (matrix[i][j]+matrix[j][i])
                elif not visit[i] and not visit[j]:
                    link += (matrix[i][j]+matrix[j][i])
        minval=min(minval,abs(start-link))
        return

    for i in range(idx,N):
        if not visit[i]:
            visit[i]=True
            back_track(i+1,depth+1)
            visit[i]=False

back_track(0,0)
print(minval)