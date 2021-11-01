import sys
read = sys.stdin.readline

T=int(read())

dp=[[0]*4 for _ in range(10001)]
dp[1][1]=dp[2][1]=dp[2][2]=dp[3][1]=dp[3][2]=dp[3][3]=1

def bottom_up(n):
    global dp
    for i in range(4,n+1):
        dp[i][3]=dp[i-3][1]+dp[i-3][2]+dp[i-3][3]
        dp[i][2]=dp[i-2][1]+dp[i-2][2]
        dp[i][1]=dp[i-1][1]

bottom_up(10000)
for _ in range(T):
    N=int(read())
    print(dp[N][1]+dp[N][2]+dp[N][3])