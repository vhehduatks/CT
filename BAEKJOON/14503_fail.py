import sys
read=sys.stdin.readline

N,M=map(int,read().split())
r,c,d=map(int,read().split())
graph=[]

for _ in range(N):
	graph.append(list(map(int,read().split())))

def robot(i,j,d,graph):
	cnt=0
	rotate_cnt=0
	i,j,d=i,j,d

	# 왼쪽 방향으로 회전 -> 북->서->남->동 -> d -1 하면 좌로 회전
	# d : 0:북, 1:동, 2:남, 3:서  -> d = 3-(d+1)%4
	d_i=[-1,0,1,0]
	d_j=[0,1,0,-1]

	while True:
		
		left_d=(d-1)%4
		left_i,left_j=i+d_i[left_d],j+d_j[left_d]
		back_d=(d-2)%4
		back_i,back_j=i+d_i[back_d],j+d_j[back_d]

		if not graph[i][j]:
			graph[i][j]=2
			cnt+=1
		
		if not graph[left_i][left_j]:
			i,j,d=left_i,left_j,left_d
			rotate_cnt=0
			continue
		
		if rotate_cnt==4:
			rotate_cnt=0
			i,j=back_i,back_j
			if graph[back_i][back_j]==1:
				break
		d=left_d
		rotate_cnt+=1
	
				
	return cnt

print(robot(r,c,d,graph))