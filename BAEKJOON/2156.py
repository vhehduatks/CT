import sys
read=sys.stdin.readline

n=int(read())
beverage=[int(read()) for _ in range(n)]

dp=[0]*n
if n>2:
	dp[0]=beverage[0]
	dp[1]=beverage[0]+beverage[1]
	dp[2]=max(beverage[0]+beverage[1],beverage[1]+beverage[2],beverage[0]+beverage[2])

	for i in range(3,n):
		dp[i]=max(
			beverage[i]+dp[i-2],
			beverage[i]+beverage[i-1]+dp[i-3]
		)
		dp[i]=max(dp[i-1],dp[i])
	print(dp[n-1])
else:
	print(sum(beverage))
