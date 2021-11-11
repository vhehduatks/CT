import sys
read=sys.stdin.readline

N,K=map(int,read().split())

dp=[[-1]*(N+1) for _ in range(K+1)]

for k in range(K+1):
    for n in range(N+1):
        if k==1:
            dp[k][n]=1
        elif n==1:
            dp[k][n]=k
        else:
            dp[k][n]=dp[k-1][n]+dp[k][n-1]

print(dp[K][N])