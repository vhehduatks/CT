import sys
read=sys.stdin.readline

n=int(read())
graph=[]*(n+1)
visit=[False]*(n+1)

for _ in range(n):
	p,c,w=map(int,read().split())
	graph[p].append((c,w))

max_deep_node=None
max_depth=0

def dfs(node,depth):
	global max_deep_node,max_depth
	if max_depth<depth:
		max_depth=depth
		max_deep_node=node
	for next_,w_ in graph[node]:
		if not visit[next_]:
			visit[next_]=True
			dfs(next_,depth+w_)
			visit[next_]=False

dfs(1,0)
max_depth=0
dfs(max_deep_node,0)
print(max_depth)
