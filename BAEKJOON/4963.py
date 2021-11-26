import sys
read=sys.stdin.readline

di=[0,0,1,-1,1,-1,-1,1]
dj=[1,-1,0,0,1,-1,1,-1]

def BFS(i,j):
    Q.append((i,j))
    visit[i][j]=True
    while Q:
        q_i,q_j=Q.pop(0)    
        for i in range(8):
            nexti=q_i+di[i]
            nextj=q_j+dj[i]

            if 0<=nexti and nexti<n and 0<=nextj and nextj<m:
                if not visit[nexti][nextj] and graph[nexti][nextj]:
                    visit[nexti][nextj]=True
                    Q.append((nexti,nextj))
    return 1

n,m=map(int,read().split())
while n+m>0:

    n,m=m,n
    Q=[]
    visit=[[False]*m for _ in range(n)]
    graph=[list(map(int,read().split())) for _ in range(n)]

    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visit[i][j]:
                cnt+=BFS(i,j)

    n,m=map(int,read().split())
    print(cnt)

