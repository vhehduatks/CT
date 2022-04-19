import sys
from copy import deepcopy
from itertools import permutations
read=sys.stdin.readline

N=int(read())

graph=[[] for _ in range(N+1)]

for _ in range(N-1):
	i,j=map(int,read().split())
	graph[i].append(j)
	graph[j].append(i)


def dfs(node):
	visit[node]=True
	path.append(node)
	for next_node in temp_graph[node]:
		if visit[next_node]==False:
			dfs(next_node)

total_path=[]
permu_graph=permutations(graph[1])
for sub_graph in permu_graph:
	temp_graph=deepcopy(graph)
	temp_graph[1]=sub_graph
	visit=[False]*(N+1)
	path=[]
	dfs(1)
	total_path.append(path)

ans=read().strip()
ret=0
for path in total_path:
	if ans==' '.join(map(str,path)):
		ret=1
		break

print(ret)