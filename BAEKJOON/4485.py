import sys
from collections import deque
read=sys.stdin.readline

N=int(read())
cnt=0

while N:
	cnt+=1
	graph=[list(map(int,read().split())) for _ in range(N)]
	cost_graph=[[sys.maxsize-1]*N for _ in range(N)]
	cost_graph[0][0]=graph[0][0]
	d_i=[0,0,1,-1]
	d_j=[1,-1,0,0]
	
	Q=deque()
	Q.append(((0,0),cost_graph[0][0]))
		
	while Q:
		node,cost=Q.popleft()
		if cost_graph[node[0]][node[1]]<cost:continue
		for k in range(4):
			next_i,next_j=node[0]+d_i[k],node[1]+d_j[k]
			if 0<=next_i<N and 0<=next_j<N:
				new_cost=cost+graph[next_i][next_j]
				if new_cost<cost_graph[next_i][next_j]:
					cost_graph[next_i][next_j]=new_cost
					Q.append(((next_i,next_j),new_cost))
	
	print(f'Problem {cnt}: {cost_graph[N-1][N-1]}')
	N=int(read())
