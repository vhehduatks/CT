import sys
from collections import deque
read=sys.stdin.readline

N=int(read())
scvs=list(map(int,read().split()))
scvs.sort(reverse=True)
heats=[9,3,1]
Q=deque()
Q.append((scvs,0))
visit=[[[False]*61 for _ in range(61)] for _ in range(61)]
ret=sys.maxsize
while Q:
	scvs_,cnt=Q.popleft()	
	if not sum(scvs_):
		ret=min(ret,cnt)
	
	for i in range(N):
		scvs_[i]-=heats[i]
		if scvs_[i]<0:scvs_[i]=0

	scvs_.sort(reverse=True)
	if not visit[scvs_[0]][scvs_[1]][scvs_[2]]:
		Q.append((scvs_,cnt+1))
		visit[scvs_[0]][scvs_[1]][scvs_[2]]=True

print(ret)