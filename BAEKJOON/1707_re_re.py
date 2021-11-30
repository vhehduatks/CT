import sys
read=sys.stdin.readline
K=int(read())

def dfs(node,c):
	global ret
	stack.append(node)
	color[node]=c
	while stack:
		sn=stack.pop()
		for next in graph[sn]:
			if color[next]==color[sn]:
				ret=1
			if visit[next]==False:
				stack.append(next)
				visit[next]=True
				color[next]=color[sn]*(-1)

for _ in range(K):
	v,e=map(int,read().split())
	graph=[[] for _ in range(v+1)]
	for _ in range(e):
		i,j=map(int,read().split())
		graph[i].append(j)
		graph[j].append(i)
	
	visit=[False]*(v+1)
	color=[0]*(v+1)
	stack=[]
	ret=0
	for i in range(1,v+1):
		if visit[i]==True:
			continue
		color=[0]*(v+1)
		stack=[]
		ret=0
		dfs(i,1)
		if ret:
			break
	print("YES" if not ret else "NO")

	
