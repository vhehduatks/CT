import sys
from collections import deque

read=sys.stdin.readline
N=int(read())
graph=[list(map(int,read().split())) for _ in range(N)]

d_i=[0,0,1,-1]
d_j=[1,-1,0,0]

visit=[[False]*N for _ in range(N)]

def dfs(i,j):
	Q.append((i,j))
	while Q:
		cur_i,cur_j=Q.popleft()
		visit[cur_i][cur_j]=True
		
		cnt=0
		for k in range(4):
			next_i,next_j=cur_i+d_i[k],cur_j+d_j[k]	
			if 0<=next_i<N and 0<=next_j<N:
				if graph[next_i][next_j]:
					if not visit[next_i][next_j]:
						Q.append((next_i,next_j))
				else:
					cnt+=1
		if cnt:
			graph[cur_i][cur_j]=-name
		else:
			graph[cur_i][cur_j]=name
				
name=1
Q=deque()
for i in range(N):
	for j in range(N):
		if graph[i][j] and not visit[i][j]:
			dfs(i,j)
			name+=1

def dfs_():
	while Q:
		cur_i,cur_j=Q.popleft()
		for k in range(4):
			next_i,next_j=cur_i+d_i[k],cur_j+d_j[k]	
			if 0<=next_i<N and 0<=next_j<N:
				if not graph[next_i][next_j] and not cost_map[next_i][next_j]:
					Q.append((next_i,next_j))
					cost_map[next_i][next_j]=cost_map[cur_i][cur_j]+1
				if graph[next_i][next_j] and abs(graph[next_i][next_j])!=n:
					return cost_map[cur_i][cur_j]

ret=sys.maxsize

for n in range(1,name):
	cost_map=[[0]*N for _ in range(N)]
	Q=deque()
	for i in range(N):
		for j in range(N):
			if graph[i][j]==-n:
				Q.append((i,j))
	ret_=dfs_()
	if ret_:			
		ret=min(ret,ret_)

print(ret)