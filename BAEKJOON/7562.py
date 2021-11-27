import sys
from collections import deque
read=sys.stdin.readline

N=int(read())

di=[-2,-1,1,2,2,1,-1,-2]
dj=[1,2,2,1,-1,-2,-2,-1]
Q=deque()
def bfs(i,j):
	Q.append((i,j))
	matrix[i][j]=1
	while Q:	
		qi,qj=Q.popleft()
		for i in range(8):
			ni=qi+di[i]
			nj=qj+dj[i]

			if 0<=ni and ni<nm and 0<=nj and nj<nm:
				if matrix[ni][nj]==0:
					matrix[ni][nj]=matrix[qi][qj]+1
					Q.append((ni,nj))

for _ in range(N):
	nm=int(read())
	sti,stj=map(int,read().split())
	edi,edj=map(int,read().split())
	matrix=[[0]*nm for _ in range(nm)]
	bfs(sti,stj)
	print(matrix[edi][edj]-1)