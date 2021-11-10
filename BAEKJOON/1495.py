import sys
read=sys.stdin.readline

N,S,M=map(int,read().split())
dp=[[False]*(M+1) for _ in range(N+1)]
arr=list(map(int,read().split()))
dp[0][S]=True
def bottom_up():
    for i in range(1,N+1):
        for j in range(M+1):
            if dp[i-1][j]:
                if j+arr[i-1]<=M:
                    dp[i][j+arr[i-1]]=True
                if j-arr[i-1]>=0:
                    dp[i][j-arr[i-1]]=True
    
    maxval=-1
    for k in range(M+1):
        if dp[N][k]:
            maxval=max(maxval,k)
    print(maxval)

bottom_up()