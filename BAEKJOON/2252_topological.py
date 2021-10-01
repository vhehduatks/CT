import sys
read=sys.stdin.readline

N,M=map(int,read().split())
graph=[[0] for _ in range(N+1)]
indegree=[0]*(N+1)

for _ in range(M):
    i,j=map(int,read().split())
    graph[i].append(j)
    indegree[j]+=1

q=[]
for i,ind in enumerate(indegree):
    if ind==0 and i!=0:
        q.append(i)

res=[]
for i in range(N):
    zero_degree=q.pop(0)
    res.append(zero_degree)
    if i==N-1:
        print(zero_degree)
    else:
        print(zero_degree,end=' ')
    
    for g in graph[zero_degree]:
        indegree[g]-=1
        if indegree[g]==0:
            q.append(g)

