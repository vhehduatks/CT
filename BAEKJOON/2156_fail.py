import sys

read=sys.stdin.readline

n=int(read())
beverage=[int(read()) for _ in range(n)]

dp=[[0]*3 for _ in range(n)]
if n>2:
	dp[2][0]=beverage[0]+beverage[1]
	dp[2][1]=beverage[0]+beverage[2]
	dp[2][2]=beverage[1]+beverage[2]

	for i in range(3,n):
		dp[i][0]=dp[i-1][2]
		dp[i][1]=dp[i-1][0]+beverage[i]
		dp[i][2]=dp[i-1][1]+beverage[i]

	print(max(dp[n-1]))
else:
	print(sum(beverage))

	
""" 
10
0
0
10
0
5
10
0
0
1
10 


"""
