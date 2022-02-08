import sys
from collections import deque
read= sys.stdin.readline
N=int(read())
graph=[[] for _ in range(N+1)]
for _ in range(N):
	i,j=map(int,read().split())
	graph[i].append(j)
	graph[j].append(i)

visit=[False]*(N+1)
stack=[]
temp=[]

def dfs(node,start):
	stack.append(node)
	cnt=0
	visit[node]=True
	while stack:
		sn=stack.pop()
		temp.append(sn)
		cnt+=1
		for next in graph[sn]:
			if not visit[next]:
				stack.append(next)
				visit[next]=True
			else:
				if cnt>1 and next==start:
					return temp	
			
	return []
Q=deque()

def bfs(node):
	Q.append(node)
	while Q:
		Qn=Q.popleft()

		if Qn in cycle:
			return cnt[Qn]
		for next in graph[Qn]:
			Q.append(next)
			visit[next]=True
			cnt[next]=cnt[Qn]+1
cycle=[]
for i in range(1,1+N):
	
	visit=[False]*(N+1)
	cycle=dfs(i,i)
	if cycle:
		break

res=[]
for i in range(1,N+1):
	if i not in cycle:
		cnt=[0]*(N+1)
		res.append(bfs(i))
	else:
		res.append(0)
print(res)