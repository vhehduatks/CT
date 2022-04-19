# https://velog.io/@junho918/Algorithm-%EB%B0%B1%EC%A4%80-16940-BFS-%EC%8A%A4%ED%8E%98%EC%85%9C-%EC%A0%80%EC%A7%80-16964-DFS-%EC%8A%A4%ED%8E%98%EC%85%9C-%EC%A0%80%EC%A7%80-python
# 탐색순서를 기반으로 정렬이 가능 먼저 방문했다 = 높은 우선순위를 가졌다 = 이걸로 정렬
import sys
read=sys.stdin.readline

N=int(read())

graph=[[] for _ in range(N+1)]
path=[]
# child_graph=[](N+1)
for _ in range(N-1):
	i,j=map(int,read().split())
	graph[i].append(j)
	graph[j].append(i)

visit=[False]*(N+1)

def dfs(node):
	visit[node]=True
	path.append(node)
	for next_node in graph[node]:
		if visit[next_node]==False:
			dfs(next_node)

order_arr=list(map(int,read().split()))

rank=[N+1]*(N+1)
for i,order in enumerate(order_arr):
	rank[order]=i

for i,g in enumerate(graph):
	if g:
		graph[i]=sorted(g,key=lambda x : rank[x])

dfs(1)

print(1 if ' '.join(list(map(str,path)))==' '.join(list(map(str,order_arr)))else 0 )

