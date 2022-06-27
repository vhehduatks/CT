N=int(input())

def in_range(i,j):
	# 상 하 좌 우 대각
	d_i=[-1,1,0,0,1,-1,-1,1]
	d_j=[0,0,-1,1,1,-1,1,-1]

	for k in range(8):
		temp_i=i
		temp_j=j
		while (0<=temp_i and temp_i<=i) and (0<=temp_j and temp_j<N):
			if graph[temp_i][temp_j]:
				return True
			temp_i+=d_i[k]
			temp_j+=d_j[k]

	return False

def recur(i,j,depth):
	global cnt,graph
	if depth==N:
		cnt+=1
		return
	for j_ in range(j,N):
		if not in_range(i,j_):
			graph[i][j_]=1
			recur(i+1,0,depth+1)
			graph[i][j_]=0

cnt=0
graph=[[0]*N for _ in range(N)]
recur(0,0,0)		
print(cnt)