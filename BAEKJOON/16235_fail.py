import sys
from collections import deque
read=sys.stdin.readline

N,M,K=map(int,read().split())
A=[[5]*(N+1) for _ in range(N+1)]
A_=[[0]*(N+1)]
A__=[[0]*(N+1) for _ in range(N+1)]
for _ in range(N):
	A_.append([0]+list(map(int,read().split())))


trees=[]

for _ in range(M):
	trees.append(list(map(int,read().split()))+[1])

trees=deque(sorted(trees,key=lambda x:-x[2]))

i_=[0,0,1,-1,1,-1,-1,1]
j_=[1,-1,0,0,1,-1,1,-1]

def is_out(i,j):
	if i<=0 or N<i or j<=0 or N<j:
		return True
	return False

cnt=0
for year in range(K):
	trees_=[]
	while trees:
		t=trees.popleft()
		if t[3]:

			if A[t[0]][t[1]]<t[2]:
				A__[t[0]][t[1]]+=(t[2]//2)
				t[3]=0
			else:
				A[t[0]][t[1]]-=t[2]
				
			t[2]+=1

			if t[3]:trees_.append(t)
			if t[2]%5==0 and t[3]:
				for k in range(8):
					next_i=t[0]+i_[k]
					next_j=t[1]+j_[k]
					if not is_out(next_i,next_j):
						trees_.append([next_i,next_j,1,1])

	
	trees+=trees_
	#trees=sorted(trees,key=lambda x:x[2])

	for n in range(1,N+1):
		for m in range(1,N+1):
			A[n][m]+=(A_[n][m]+A__[n][m])
			A__[n][m]=0

print(len(trees))