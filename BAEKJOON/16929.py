import sys
read=sys.stdin.readline

N,M=map(int,read().split())

graph=[]
for _ in range(N):
	temp=list(read().strip())
	graph.append(temp)
stack=[]
visit=[[False]*M for _ in range(N)]
di=[0,0,1,-1]
dj=[1,-1,0,0]
cycle=False
def dfs(i,j):
	global cycle
	stack.append((i,j))
	visit[i][j]=True


	while stack:
		si,sj=stack.pop()
		istwo=0
		for i in range(4):
			ni=si+di[i]
			nj=sj+dj[i]

			if 0<=ni and ni<N and 0<=nj and nj<M:
				if graph[ni][nj]==graph[si][sj]:
					if visit[ni][nj]==True:
						istwo+=1
					else:
						stack.append((ni,nj))
						visit[ni][nj]=True
			if istwo>1:
				cycle=True
				break
		if cycle:
			break
	
	return cycle

for i in range(N):
	for j in range(M):
		if not visit[i][j]:
			ret=dfs(i,j)
		if cycle:
			break
	if cycle:
		break

print('Yes' if ret else 'No')