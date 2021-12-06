import sys
from collections import deque
sys.setrecursionlimit(10**6)
read=sys.stdin.readline

N=int(read())
graph=[[] for _ in range(N+1)]

for _ in range(N):
	i,j=map(int,read().split())
	graph[i].append(j)
	graph[j].append(i)




def dfs(start,node,cnt):
	global cycle
	stack.append(node)
	visit[node]=True

	for next in graph[node]:
		if cnt>1 and start==next:
			cycle=stack[:]
		elif not visit[next]:
			dfs(start,next,cnt+1)
			stack.pop()

		

cycle=[]
for i in range(1,N+1):
	if not cycle:
		stack=[]
		visit=[False]*(N+1)
		dfs(i,i,0)
		


def bfs(node):
	global cnt
	Q.append(node)
	visit[node]=True
	cnt[node]=0
	while Q:
		qn=Q.popleft()
		for next in graph[qn]:
			if next in cycle:
				return cnt[qn]+1
			elif not visit[next]:
				Q.append(next)
				visit[next]=True
				cnt[next]=cnt[qn]+1
			
res=[]

for i in range(1,N+1):

	if not i in cycle:
		cnt=[0]*(N+1)
		Q=deque()
		visit=[False]*(N+1)
		res.append(bfs(i))	
	else:
		res.append(0)

print(" ".join(list(map(str,res))))
