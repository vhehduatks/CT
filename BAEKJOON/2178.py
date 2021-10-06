import sys
read=sys.stdin.readline
N,M=map(int,read().split())
graph=[]
visit=[[False]*M for _ in range(N)]

for _ in range(N):
    temp=list(map(int,list(read().strip())))
    graph.append(temp)

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(i,j):
    global graph
    q=[]
    q.append((i,j))
    visit[i][j]=True
    while q:
        q_i,q_j=q.pop(0)
        for k in range(4):
            next_i=q_i+dy[k]
            next_j=q_j+dx[k]

            if (0<=next_i and next_i<N) and (0<=next_j and next_j<M):

                if graph[next_i][next_j]!=0 and visit[next_i][next_j]==False:
                    q.append((next_i,next_j))
                    visit[next_i][next_j]=True
                    graph[next_i][next_j]+=graph[q_i][q_j]
    
    return graph[N-1][M-1]

print(bfs(0,0))