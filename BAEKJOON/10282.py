import sys
from collections import deque
read=sys.stdin.readline
TC=int(read())

for _ in range(TC):
	n,d,c=map(int,read().split())
	graph=[[] for _ in range(n+1)]
	dist_list=[sys.maxsize]*(n+1)
	dist_list[c]=0

	for _ in range(d):
		a,b,s=map(int,read().split())
		graph[b].append([a,s])

	Q=deque()
	Q.append((c,dist_list[c]))

	while Q:
		node,dist=Q.popleft()
		if dist_list[node]<dist:continue
		for next_,dist_ in graph[node]:
			new_dist=dist+dist_
			if new_dist<dist_list[next_]:
				dist_list[next_]=new_dist
				Q.append((next_,new_dist))

	max_far=0
	cnt=0
	for d in dist_list:
		if d != sys.maxsize:
			cnt+=1
			max_far=max(max_far,d)

	print(f'{cnt} {max_far}')



