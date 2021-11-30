import sys
read=sys.stdin.readline

K=int(read())
def dfs(node,c):
	global ret,depth
	stack.append(node)
	color[node]=c*(-1)
	visit[node]=True
	for next in graph[node]:
		if color[next]==color[node]:
			ret=0
		if visit[next]==False:
			dfs(next,color[node])
			visit[next]=False
			
	stack.pop()

for _ in range(K):
	v,e=map(int,read().split())
	graph=[[] for _ in range(v+1)]
	for _ in range(e):
		i,j=map(int,read().split())
		graph[i].append(j)
		graph[j].append(i)
	ret=1
	stack=[]	
	color=[0]*(v+1)
	visit=[False]*(v+1)

	for i in range(1,v+1):
		if visit[i]==True:
			continue
		ret=1
		depth=0
		stack=[]	
		color=[0]*(v+1)
		dfs(i,1)
		if not ret:
			break
	print("YES" if ret else "NO")