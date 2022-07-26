from collections import deque
import sys
read=sys.stdin.readline

N=int(read())
graph=[list(map(int,read().split())) for _ in range(N)]

name=1
visit=[[False]*N for _ in range(N)]

d_i=[0,0,1,-1]
d_j=[1,-1,0,0]
def bfs(i,j):
	global name
	Q=deque()
	Q.append((i,j))
	name+=1
	while Q:
		cur_i,cur_j=Q.popleft()
		visit[cur_i][cur_j]=True
		graph[cur_i][cur_j]=name
		for k in range(4):
			next_i,next_j=cur_i+d_i[k],cur_j+d_j[k]
			if 0<=next_i<N and 0<=next_j<N:
				if not visit[next_i][next_j] and graph[next_i][next_j]:
					Q.append((next_i,next_j))

for i in range(N):
	for j in range(N):
		if graph[i][j]==1 and not visit[i][j]:
			bfs(i,j)


def bfs_(i,j,n):
	visit_[n]=True
	visit=[[False]*N for _ in range(N)]
	cost_map=[[0]*N for _ in range(N)]
	Q=deque()
	Q.append((i,j))
	while Q:
		cur_i,cur_j=Q.popleft()
		visit[cur_i][cur_j]=True
		for k in range(4):
			next_i,next_j=cur_i+d_i[k],cur_j+d_j[k]
			if 0<=next_i<N and 0<=next_j<N:
				if graph[next_i][next_j] and graph[next_i][next_j]!=n:
					visit_[graph[next_i][next_j]]=True	
					ret=sys.maxsize
					for i in range(4):
						next_i_,next_j_=next_i+d_i[i],next_j+d_j[i]
						if 0<=next_i_<N and 0<=next_j_<N:
							if cost_map[next_i_][next_j_]:
								ret=min(ret,cost_map[next_i_][next_j_])
					return ret
				if not visit[next_i][next_j] and not graph[next_i][next_j]:
					Q.append((next_i,next_j))
					cost_map[next_i][next_j]=cost_map[cur_i][cur_j]+1
	return 0

ret=sys.maxsize
visit_=[False]*(name+1)
for i in range(N):
	for j in range(N):
		if graph[i][j]:
			if not visit_[graph[i][j]]:
				temp=bfs_(i,j,graph[i][j])
				if temp:
					ret=min(ret,temp)

print(ret)
