import sys

read=sys.stdin.readline

N,M=map(int,read().split())
r,c,d=map(int,read().split())
graph=[]

for _ in range(N):
	graph.append(list(map(int,read().split())))

d_i=[-1,0,1,0]
d_j=[0,1,0,-1]
ret=0
def recur(i,j,d):
	global ret
	if not graph[i][j]:
		# graph를 변형시키면서 재귀가 들어가므로 한번의 dfs 만 수행된다. 해당 dfs는 문제의 조건으로 진행되므로 ㄱㅊ
		ret+=1
		graph[i][j]=2

	for _ in range(4):
		leftd=(d+3)%4
		next_i=i+d_i[leftd]
		next_j=j+d_j[leftd]
		# 조건문 밑에 재귀가 있고 바로 return 이 있으므로 재귀로 들어가면 한번 수행하고 끝나버림.
		if not graph[next_i][next_j]:
			recur(next_i,next_j,leftd)
			return
		d=leftd
	
	backd=(d+2)%4
	next_i=i+d_i[backd]
	next_j=j+d_j[backd]
	if graph[next_i][next_j]==1:
		return
	recur(next_i,next_j,d)

recur(r,c,d)
print(ret)

