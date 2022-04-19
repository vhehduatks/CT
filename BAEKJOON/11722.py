import sys
read=sys.stdin.readline

N=int(read())
arr=list(map(int,read().split()))

dp=[1]*N

for i in range(N-1,-1,-1):
	for j in range(N-1,i,-1):
		if arr[i]>arr[j]:
			dp[i]=max(dp[i],dp[j]+1)

print(max(dp))
