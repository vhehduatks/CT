"""
로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 북쪽에서부터 r번째, 서쪽에서부터 c번째로 위치한 칸은 (r, c)로 나타낼 수 있다.

로봇 청소기는 다음과 같이 작동한다.

1현재 위치를 청소한다.
2현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다.
	a 현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다. 
		그렇지 않을 경우, 왼쪽 방향으로 회전한다. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.
	b 1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 작동을 멈춘다. 그렇지 않다면 한 칸 후진한다.
"""

import sys
read=sys.stdin.readline

N,M=map(int,read().split())

r,c,d=map(int,read().split())
# 0:북, 1:동, 2:남, 3:서

d_i=[-1,0,1,0]
d_j=[0,-1,0,1]

graph=[]

for _ in range(N):
	graph.append(list(map(int,read().split())))
visit=[[False]*51 for _ in range(51)]

cleaning=0
next_i,next_j=r,c
def dfs(i,j):
	global cnt
	rotate_cnt=0
	if not visit[i][j]:
		visit[i][j]=True
		cleaning+=1

	left_coord=(d_i[d+1],d_j[d+1])
	
	while not visit[left_coord[0]][left_coord[1]] or rotate_cnt<3:
		d+=1
		rotate_cnt+=1
		next_i,next_j=left_coord[0],left_coord[1]
		dfs(next_i,next_j)
	next_i,next_j=d_i[d+2],d_j[d+2]
	if graph[next_i][next_j]:
		return
	dfs(next_i,next_j)
	
		

