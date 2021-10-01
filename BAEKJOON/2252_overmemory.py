import sys
read=sys.stdin.readline
N,M=map(int,read().split())
matrix=[[0]*(N+1) for _ in range(N+1)]
topological=[]

for _ in range(M):
    i,j=map(int,read().split())
    matrix[i][j]=1


j=1
while(len(topological)<N):


    input=0
    for i in range(1,N+1):
        if j in topological:
            input=-1
            continue
        input+=matrix[i][j]
    if input==0:
        print(j,end=' ')
        topological.append(j)
        matrix[j]=[0]*(N+1)
        j=0
    j+=1
    
    if len(topological)==N:
        print('')

    
    
