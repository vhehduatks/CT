import sys

read=sys.stdin.readline

N,M=map(int,read().split())

office=[[0]*N for _ in range(M)]
cctv=[]
wall_i=[]
wall_j=[]

for i in range(N):
	temp=list(map(int,read().split()))
	for j,t in enumerate(temp):
		if t:
			if t==6:
				wall_i.append(i)
				wall_j.append(j)
			else:
				cctv.append([i,j,t])

#case={1:1,2:2,}

def is_wall(c_i,c_j):
	ret=False
	wall_i_idx,wall_j_idx=-1,-1#=max(N-c_i+1,c_i),max(M-c_j+1,c_j)
	if c_i in wall_i:
		ret=True
		wall_i_idx=wall_i.index(c_i)
	if c_j in wall_j:
		ret=True
		wall_j_idx=wall_j.index(c_j)
	if ret:
		return ret,wall_i_idx,wall_j_idx
	return ret,wall_i_idx,wall_j_idx

def change_office(init,end,d):


for c in cctv:
	if c[2]==1:
		j_len=0
		i_len=0
		wall,wall_i_idx,wall_j_idx=is_wall(c[0],c[1])
		if wall:
			if wall_i_idx>0:
				if c[1]<wall_j[wall_i_idx]:
					# cctv<wall
					j_len=max(c[1],wall_j[wall_i_idx]-c[1])
				else:
					# wall<cctv
					j_len=max(c[1]-wall_j[wall_i_idx],M-c[1])

			if wall_j_idx>0:
				if c[0]<wall_i[wall_j_idx]:
					# cctv<wall
					i_len=max(c[0],wall_j[wall_j_idx]-c[0])
				else:
					# wall<cctv
					i_len=max(c[0]-wall_j[wall_j_idx],N-c[0])
		else:
			j_len=max(c[1],M-c[1])
			i_len=max(c[0],N-c[0])
	elif c[2]==2:
		pass
	elif c[2]==3:
		pass
	elif c[2]==4:
		pass
	elif c[2]==5:
		pass



