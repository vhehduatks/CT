import sys
read=sys.stdin.readline

N,M=map(int,read().split())

graph=[[] for _ in range(N+1)]
for _ in range(M):
	i,j=map(int,read().split())
	graph[i].append(j)
	graph[j].append(i)

visit=[False]*(N+1)
stack=[]
cnt=0
def dfs(node):
	global cnt
	stack.append(node)
	visit[node]=True
	if len(stack)==5:
		cnt+=1
		stack.pop()
		return 
	for next in graph[node]:
		if not visit[next]:
			dfs(next)	
			visit[next]=False
	stack.pop()	

for i in range(N+1):
	visit=[False]*(N+1)
	dfs(i)	
	if cnt:
		break
print(1 if cnt!=0 else 0)
