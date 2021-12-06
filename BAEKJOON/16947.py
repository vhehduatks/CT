import sys
from collections import deque
read=sys.stdin.readline

N=int(read())
graph=[[] for _ in range(N+1)]
for _ in range(N):
	i,j=map(int,read().split())
	graph[i].append(j)
	graph[j].append(i)

def dfs(start,node,cnt):
	stack.append(node)
	visit[node]=True
	if cnt>=2 and node==start:
		for i in stack:
			cycle[i]=True	
		stack.pop()
		return
	for next in graph[node]:
		if not visit[next]:
			dfs(start,next,cnt+1)
			visit[next]=False
	stack.pop()	

def bfs(node):
	Q.append(node)
	visit[node]=True
	while Q:
		Qn=Q.popleft()
		if cycle[Qn]:
			return cnt[Qn]
		for next in graph[Qn]:
			if not visit[next]:
				Q.append(next)
				visit[next]=True
				cnt[next]=cnt[Qn]+1

Q=deque()
stack=[]
visit=[False]*(N+1)
cycle=[False]*(N+1)

for i in range(1,N+1):
	dfs(i,i,0)
cnt=[0]*(N+1)
ret=[]
for i in range(1,N+1):
	if not cycle[i]:
		ret.append(bfs(i))
	else:
		ret.append(0)

print(ret)