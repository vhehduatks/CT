import sys
sys.setrecursionlimit(10**6)
read=sys.stdin.readline

N=int(read())
A=list(map(int,read().split()))

dp=[1001]*N

def recur(depth):
	if depth==N-1:
		if N==1:
			dp[0]=0
		return 0
	
	if dp[depth]!=1001:
		return dp[depth]

	for i in range(1,A[depth]+1):
		if i+depth<N:
			dp[depth]=min(dp[depth],recur(depth+i)+1)
	
	return dp[depth]

recur(0)
print(dp[0] if dp[0]<1001 else -1)
