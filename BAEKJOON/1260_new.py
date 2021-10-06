import sys
sys.setrecursionlimit(10**8)
read=sys.stdin.readline

N,M,I=map(int,read().split())
visit=[False]*(N+1)
graph=[[]for _ in range(N+1)]

for _ in range(M):
    i,j=map(int,read().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(node):
    print(node,end=' ')
    visit[node]=True
    for next_node in graph[node]:
        if visit[next_node]==False:
            dfs(next_node)

q=[]
def bfs(node):
    print(node,end=' ')
    visit[node]=True
    for next_node in graph[node]:
        if visit[next_node]==False and next_node not in q:
            q.append(next_node)
    
    if q:
        bfs(q.pop(0))

dfs(I)
print('')
visit=[False]*(N+1)
bfs(I)
print('')