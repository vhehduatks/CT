import sys
read=sys.stdin.readline
mod=10007
n=int(read())

dp=[0]*(1001)

dp[1]=1
dp[2]=2
for i in range(3,n+1):
	dp[i]=(dp[i-1]+dp[i-2])%mod

print(dp[n])