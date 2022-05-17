import sys
read=sys.stdin.readline

n=int(read())

card=list(map(int,read().split()))
card.insert(0,0)
dp=[sys.maxsize-1]*(n+1)

dp[1]=card[1]

for i in range(1,n+1):
	for j in range(1,i):
		dp[i]=min(card[i],dp[i-j]+dp[j],dp[i])

print(dp[n])