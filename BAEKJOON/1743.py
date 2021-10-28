import sys
from types import GeneratorType
read = sys.stdin.readline


N,M,K=map(int,read().split())
graph=[[0]*M for _ in range(N)]
visit=[[False]*M for _ in range(N)]

for _ in range(K):
    i,j=map(int,read().split())
    graph[i-1][j-1]=1

direc_i=[-1,1,0,0]
direc_j=[0,0,-1,1]

def bfs(i,j):
    q=[]
    visit[i][j]=True
    q.append((i,j))
    ret=1
    while q:
        q_i,q_j=q.pop(0)
        for k in range(4):
            next_i=q_i+direc_i[k]
            next_j=q_j+direc_j[k]

            if 0<=next_i and next_i<N and 0<=next_j and next_j<M:
                if visit[next_i][next_j]==False:
                    visit[next_i][next_j]=True
                    if graph[next_i][next_j]==1:
                        q.append((next_i,next_j))
                        ret+=1

    return ret

maxval=0
for i in range(N):
    for j in range(M):
        if graph[i][j]==1 and visit[i][j]==False:
            maxval=max(maxval,bfs(i,j))

print(maxval)
