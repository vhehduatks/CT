import sys
from copy import deepcopy

read=sys.stdin.readline

n=int(read())

graph=[]

for _ in range(n):
	graph.append(list(map(int,read().split())))
dp=[[0]*n for _ in range(n)]

"""
recur(i,j):
	if dp[i][j]:
		return dp[i][j]
	if i==n-1:
		return max(graph[i][j],graph[i][j+1])

	ret=-1
	
	ret=max(recur(i+1,j)+graph[i][j],recur(i+1,j+1)+graph[i][j])
	dp[i][j]=ret
	return ret
"""

def recur(i,j):
	if dp[i][j]:
		return dp[i][j]
	if i==n-1:
		return graph[i][j]
	
	dp[i][j]=max(recur(i+1,j)+graph[i][j],recur(i+1,j+1)+graph[i][j])
	return dp[i][j]

print(recur(0,0))
