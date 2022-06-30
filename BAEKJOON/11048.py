import sys
sys.setrecursionlimit(10**6)
read=sys.stdin.readline


N,M=map(int,read().split())

graph=[list(map(int,read().split())) for _ in range(N)]
dp=[[-1]*M for _ in range(N)]

def recur(i,j):
	if i>=N or j>=M:
		return 0
	if dp[i][j] != -1:
		return dp[i][j]	
	ret=0
	ret=max(recur(i+1,j),recur(i,j+1),recur(i+1,j+1))+graph[i][j]
	dp[i][j]=ret
	return ret

recur(0,0)
print(dp[0][0])