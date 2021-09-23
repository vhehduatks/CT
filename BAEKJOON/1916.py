import sys 
import heapq
read=sys.stdin.readline

N=int(read())
M=int(read())
Q=[]
graph=[[sys.maxsize-1]*(N+1) for _ in range(N+1)]
distance=[sys.maxsize-1]*(N+1)

for _ in range(M):
    i,j,weight=map(int,read().split())
    if weight<graph[i][j]:
        graph[i][j]=weight

start,end=map(int,read().split())
distance[start]=0
heapq.heappush(Q,(distance[start],start))
while Q:
    weight,node=heapq.heappop(Q)

    if distance[node]<weight:
        continue
    
    for i,adj_weight in enumerate(graph[node],start=0):
        
        cost=weight+adj_weight
        if cost<distance[i] and i!=node:
            distance[i]=cost
            heapq.heappush(Q,(cost,i))

print(distance[end])