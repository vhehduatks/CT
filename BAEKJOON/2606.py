import sys
read=sys.stdin.readline

N=int(read())
K=int(read())
visit=[False]*(N+1)
graph=[[] for _ in range(N+1)]

for _ in range(K):
    i,j=map(int,read().split())
    graph[i].append(j)
    graph[j].append(i)

cnt=0
q=[1]
visit[1]=True
while q:
    node=q.pop(0)
    for next_node in graph[node]:
        if visit[next_node]==False and next_node not in q:
            q.append(next_node)
            visit[next_node]=True
            cnt+=1
print(cnt)