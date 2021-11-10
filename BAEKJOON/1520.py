import sys
sys.setrecursionlimit(9999)
read=sys.stdin.readline

M,N=map(int,read().split())
matrix=[]
for _ in range(M):
    temp=list(map(int,read().split()))
    matrix.append(temp)

dp=[[-1]*(N) for _ in range(M)]

iarr=[0,0,1,-1]
jarr=[1,-1,0,0]
def path(i,j):
    if i==M-1 and j==N-1:
        return 1

    if dp[i][j]!=-1:
        return dp[i][j]

    dp[i][j]=0

    for k in range(4):
        nexti,nextj=i+iarr[k],j+jarr[k]
        if -1<nexti and nexti<M and -1<nextj and nextj<N:
            if matrix[nexti][nextj]<matrix[i][j]:
                dp[i][j]+=path(nexti,nextj)
    return dp[i][j]

print(path(0,0))

