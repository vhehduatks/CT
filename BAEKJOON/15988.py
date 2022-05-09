import sys
read=sys.stdin.readline
mod=1000000009
n=int(read())

dp=[0]*1000001
dp[1],dp[2],dp[3]=1,2,4

for i in range(4,1000001):
	dp[i]=(dp[i-1]%mod+dp[i-2]%mod+dp[i-3]%mod)%mod

for _ in range(n):
	print(dp[int(read())])
