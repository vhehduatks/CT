import sys
read=sys.stdin.readline

N,M,K=map(int,read().split())
A=[[5]*(N+1) for _ in range(N+1)]
A_=[[0]*(N+1)]
for _ in range(N):
	A_.append([0]+list(map(int,read().split())))


trees=[]
for _ in range(M):
	trees.append(list(map(int,read().split()))+[1])
trees=sorted(trees,key=lambda x:x[2])


# def Spring(a,trees):
# 	for i,t in enumerate(trees):	
# 		if a[t[0]][t[1]]<t[2]:
# 			trees_[i]=False

# def Summer(a,trees):
# 	for i,t in enumerate(trees):
# 		if not trees_[i]:
# 			a[t[0]][t[1]]+=(t[2]//2)

# def fall() 		

i_=[0,0,1,-1,1,-1,-1,1]
j_=[1,-1,0,0,1,-1,1,-1]
def is_out(i,j):
	if i<=0 or N<i or j<=0 or M<j:
		return True
	return False

cnt=0
for year in range(K+1):
	trees_=[]
	for t in trees:
		if t[3]:
			t[2]+=1
			if A[t[0]][t[1]]<t[2]:
				A[t[0]][t[1]]+=(t[2]//2)
				t[3]=0
			else:
				A[t[0]][t[1]]-=t[2]
	
			if t[2]%5==0 and t[3]:
				for k in range(8):
					next_i=t[0]+i_[k]
					next_j=t[1]+j_[k]
					if not is_out(next_i,next_j):
						trees_.append([next_i,next_j,1,1])

	
		

		if year==K and t[3]:
			cnt+=1
	trees+=trees_
	trees=sorted(trees,key=lambda x:x[2])
	for n in range(1,N+1):
		for m in range(1,M+1):
			A[n][m]+=A_[n][m]

print(cnt)