import sys
read=sys.stdin.readline

m,n=map(int,read().split())

def bfs():
	while Q:
		qi,qj=Q.pop(0)

		for i in range(4):
			ni=qi+di[i]
			nj=qj+dj[i]

			if 0<=ni and ni<n and 0<=nj and nj<m:
				if tmt[ni][nj]==1 or tmt[ni][nj]==0:
					tmt[ni][nj]=tmt[qi][qj]+1
					Q.append((ni,nj))

tmt=[]
for _ in range(n):
	tmt.append(list(map(int,read().split())))	

Q=[]
di=[0,0,1,-1]
dj=[1,-1,0,0]
for i in range(n):
	for j in range(m):
		if tmt[i][j]==1:
			Q.append((i,j))

bfs()
def dayfunc():	
	day=0
	for i in range(n):
		for j in range(m):
			if tmt[i][j]==0:
				return -1					
			day=max(day,tmt[i][j])
	return day-1

print(dayfunc())