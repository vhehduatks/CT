import sys
from collections import deque
read=sys.stdin.readline

TC=int(read())

for _ in range(TC):
	n,d,c=map(int,read().split())
	graph=[[-1]*(n+1) for _ in range(n+1)]
	cost_list=[sys.maxsize]*(n+1)
	cost_list[c]=0
	visit=[False]*(n+1)
	Q=deque()
	
	for _ in range(d):
		a,b,s=map(int,read().split())
		graph[b][a]=s

	Q.append((c,cost_list[c]))
	cnt=0
	while Q:
		node,cost=Q.popleft()
		if not visit[node]:
			cnt+=1
			visit[node]=True
		if cost_list[node]<cost:continue
		for next_,cost_ in enumerate(graph[node]):
			if cost_!=-1:
				new_cost=cost+cost_
				if new_cost<cost_list[next_]:
					cost_list[next_]=new_cost
					Q.append((next_,new_cost))

	print(f'{cnt} {cost_list[n]}')