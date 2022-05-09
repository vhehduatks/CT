import sys
read=sys.stdin.readline

n=int(read())

dp=[0]*100
dp[1],dp[2],dp[3]=1,2,4

for i in range(4,100):
	dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for _ in range(n):
	print(dp[int(read())])
