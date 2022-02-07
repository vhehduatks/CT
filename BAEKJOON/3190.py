import sys
read=sys.stdin.readline

N=int(read())
K=int(read())
graph=[[0]*N for _ in range(N)]

for _ in range(K):
	i,j=map(int,read().split())
	graph[i][j]=1

L=int(read())
command=[]
for _ in range(L):
	command.append((read().strip().split()))

score=cnt=i=j=direction=0

di=[0,1,0,-1]
dj=[1,0,-1,0]
class Snake:
	def __init__(self) -> None:
		self.head_i=0
		self.head_j=0
		self.score=0
		self.body=[]
	def _move(self):
		

snake=Snake()


otime,order=command.pop(0)
while score<K:
	
	if cnt==int(otime):
		if order=='D':
			direction+=1
		else:
			direction-=1
		if command:
			otime,order=command.pop(0)
	i=i+di[direction]
	j=j+dj[direction]

	if i<0 or i>N or j<0 or j>N :
		cnt+=1
		break

	if graph[i][j]:
		score+=1
		graph[i][j]=0

	cnt+=1


print(cnt)
