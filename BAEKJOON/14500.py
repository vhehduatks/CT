import sys

read=sys.stdin.readline

N,M=map(int,read().split())
graph=[]
visit=[[False]*M for _ in range(N)]

for _ in range(N):
	graph.append(list(map(int,read().split())))

def is_out(i,j):
	if i<0 or N<=i or j<0 or M<=j:
		return True
	return False

i_=[0,-1,1,0]
j_=[1,0,0,-1]
path=[]
score=-(sys.maxsize-1)

def search_T(i,j):
	global score
	direction={
		'up':[(i,j),(i-1,j),(i,j-1),(i,j+1)],
		'down':[(i,j),(i+1,j),(i,j-1),(i,j+1)],
		'left':[(i,j),(i-1,j),(i+1,j),(i,j-1)],
		'right':[(i,j),(i-1,j),(i+1,j),(i,j+1)]
		}
	for _,item in direction.items():
		path=[]
		for next_i,next_j in item:	
			if is_out(next_i,next_j):
				break
			path.append(graph[next_i][next_j])
		if len(path)==4:
			score=max(score,sum(path))


def dfs(i,j):
	global score
	
	if len(path)>=4:
		score=max(score,sum(path))
		return
	
	for k in range(4):
		next_i=i+i_[k]
		next_j=j+j_[k]
		if not is_out(next_i,next_j):
			if not visit[next_i][next_j]:
				visit[next_i][next_j]=True
				path.append(graph[next_i][next_j])
				dfs(next_i,next_j)
				path.pop()
				visit[next_i][next_j]=False

for n in range(N):
	for m in range(M):
		visit[n][m]=True
		path.append(graph[n][m])
		dfs(n,m)
		path.pop()
		visit[n][m]=False
		search_T(n,m)

print(score)

