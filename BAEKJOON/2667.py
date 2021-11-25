import sys
read=sys.stdin.readline

N=int(read())
graph=[]

for _ in range(N):
    temp=list(map(int,list(read().strip())))
    graph.append(temp)

visit=[[False]*N for _ in range(N)]

Q=[]
def BFS(i,j):
    cnt=0
    if visit[i][j] or graph[i][j]==0:
        return cnt
    Q.append((i,j)) 
    visit[i][j]=True
    cnt+=1
    di=[0,0,-1,1]
    dj=[-1,1,0,0]
    while Q:
        q_i,q_j=Q.pop(0)

        for i in range(4):
            nexti=q_i+di[i]
            nextj=q_j+dj[i]
            if 0<=nexti and nexti<N and 0<=nextj and nextj<N:
                if not visit[nexti][nextj] and graph[nexti][nextj]==1:
                    visit[nexti][nextj]=True
                    Q.append((nexti,nextj))
                    cnt+=1
    return cnt

incnt_arr=[]
outcnt=0
for i in range(N):
    for j in range(N):
        temp=BFS(i,j)
        if temp:
            outcnt+=1
            incnt_arr.append(temp)
if not incnt_arr:
    incnt_arr.append(0)
incnt_arr.sort(reverse=False)
print(outcnt)
print('\n'.join(map(str,incnt_arr)))
