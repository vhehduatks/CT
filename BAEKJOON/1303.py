import sys
read=sys.stdin.readline

N,M=map(int,read().split())

graph=[]
for _ in range(M):
    temp=list(read().strip())
    graph.append(temp)

visit=[[False]*N for _ in range(M)]
x=[0,0,-1,1]
y=[-1,1,0,0]
def bfs_cheak(i,j,color):
    if visit[i][j]==True or graph[i][j]!=color:
        return 0
    visit[i][j]=True
    q=[(i,j)]
    ret=1
    while q:
        q_i,q_j=q.pop(0)
        for k in range(4):
            next_i=q_i+y[k]
            next_j=q_j+x[k]

            if (0<=next_i and next_i<M) and (0<=next_j and next_j<N) and visit[next_i][next_j]==False:
                if graph[next_i][next_j]==color:
                    q.append((next_i,next_j))
                    ret+=1
                    visit[next_i][next_j]=True
            
    return ret

white=0
blue=0
for i in range(M):
    for j in range(N):
            white+=bfs_cheak(i,j,'W')**2
            blue+=bfs_cheak(i,j,'B')**2

print(white,blue)