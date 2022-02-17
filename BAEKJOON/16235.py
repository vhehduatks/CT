import sys
read=sys.stdin.readline

N,M,K=map(int,read().split())

tree_map=[[[] for _ in range(N+1)] for _ in range(N+1)] # ^^
A=[[5]*(N+1) for _ in range(N+1)]
A_=[[0]*(N+1)]
for _ in range(N):
	A_.append([0]+list(map(int,read().split())))


for _ in range(M):
	i,j,k=map(int,read().split())
	tree_map[i][j].append(k)

def spring_and_summer(tree_map):
	for i in range(1,1+N):
		for j in range(1,1+N):
			die=0
			idx=0
			for k,t in enumerate(tree_map[i][j]):
				if die:
					A[i][j]+=(tree_map[i][j][k]//2)
					continue
				if A[i][j]-t>=0:
					tree_map[i][j][k]+=1
					A[i][j]-=t
				else:
					A[i][j]+=(tree_map[i][j][k]//2)
					die=1
					idx=k
				
			if die:
				tree_map[i][j]=tree_map[i][j][:idx] # tree_map = 나무의 좌표로 나이가 저장-< 나이가 리스트로 저장


i_=[0,0,1,-1,1,-1,-1,1]
j_=[1,-1,0,0,1,-1,1,-1]

def is_out(i,j):
	if i<=0 or N<i or j<=0 or N<j:
		return True
	return False

def fall_and_winter(tree_map):
	for i in range(1,1+N):
		for j in range(1,1+N):
			t_len=len(tree_map[i][j])
			for t in range(t_len):
				if tree_map[i][j][t]%5==0:
					for k in range(8):
						next_i=i+i_[k]
						next_j=j+j_[k]
						if not is_out(next_i,next_j):
							tree_map[next_i][next_j].append(1)
							tree_map[next_i][next_j].insert(0,tree_map[next_i][next_j])
			A[i][j]+=A_[i][j]					

for _ in range(K):
	spring_and_summer(tree_map)
	fall_and_winter(tree_map)


cnt=0
for i in range(1,1+N):
	for j in range(1,1+N):
		cnt+=len(tree_map[i][j])			
print(cnt)
