import sys
read=sys.stdin.readline
MOD=9901

N=int(read())
"""
dp[n][0] : xx 
dp[n][1] : ox
dp[n][2] : xo

dp[n][0] = dp[n-1][0] + dp[n-1][1] + dp[n-1][2]
dp[n][1] = dp[n-1][0] + dp[n-1][2]
dp[n][2] = dp[n-1][0] + dp[n-1][1]
숫자 자체의 용량도 생각할것
"""
dp=[[0]*3 for _ in range(100000)]
dp[0][0],dp[0][1],dp[0][2]=1,1,1

for i in range(1,N):
	dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%MOD
	dp[i][1] = (dp[i-1][0] + dp[i-1][2])%MOD
	dp[i][2] = (dp[i-1][0] + dp[i-1][1])%MOD

print(sum(dp[N-1])%MOD)	


