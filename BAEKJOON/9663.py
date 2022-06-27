N=int(input())
graph=[0]*N

def in_range(j):
	for j_ in range(j):
		if graph[j_]==graph[j] or (abs(graph[j_]-graph[j])==abs(j-j_)):
			return True
	return False
	
def recur(depth):
	global cnt
	if depth==N:
		cnt+=1
		return
	
	for j in range(N):
		graph[depth]=j
		if not in_range(depth):
			recur(depth+1)
cnt=0
recur(0)
print(cnt)	