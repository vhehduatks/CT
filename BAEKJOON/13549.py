import sys
from collections import deque
read=sys.stdin.readline

N,K=map(int,read().split())

Q=deque()
visit=[False]*100001

Q.append((N,0))
ret=sys.maxsize
while Q:
	n,cnt=Q.popleft()
	visit[n]=True
	if n==K:
		ret=min(ret,cnt)
	for i,n_ in enumerate([n*2,n-1,n+1]):
		if 0<=n_<=100000:
			if visit[n_]:continue
			if i:
				Q.append((n_,cnt+1))
			else:
				Q.append((n_,cnt))

print(ret)
