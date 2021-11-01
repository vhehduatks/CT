import sys
read=sys.stdin.readline

mod=1000000009
dp=[[0]*4 for _ in range(100001)]

dp[1][1]=dp[2][2]=dp[3][1]=dp[3][2]=dp[3][3]=1

def bottom_up(n):
    global dp
    for i in range(4,n+1):
        dp[i][3]=(dp[i-3][1]+dp[i-3][2])%mod
        dp[i][2]=(dp[i-2][1]+dp[i-2][3])%mod
        dp[i][1]=(dp[i-1][2]+dp[i-1][3])%mod

bottom_up(100000)


T=int(read())
for _ in range(T):
    N=int(read())
    print(sum(dp[N])%mod)