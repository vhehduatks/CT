from collections import deque
import sys

read=sys.stdin.readline

N=int(read())
graph=[[] for _ in range(N+1)]

for _ in range(N-1):
	i,j=map(int,read().split())
	graph[i].append(j)
	graph[j].append(i)

visit=[False]*(N+1)
path=[]

def bfs(node):
	q=deque()
	q.append(node)
	while q:
		q_node=q.popleft()	
		path.append(q_node)
		for next_node in graph[q_node]:
			if not visit[next_node]:
				# if not next_node in q: # q 체크를 하지 않는것이 시간복잡도 면에서 이득을 본다.
				q.append(next_node)
				visit[q_node]=True

order_arr=list(map(int,read().split()))

rank=[N]*(N+1)

for i,val in enumerate(order_arr):
	rank[val]=i

for i,g in enumerate(graph):
	if g:
		graph[i]=sorted(g,key=lambda x:rank[x])	

bfs(1)

print(1 if path==order_arr else 0)

