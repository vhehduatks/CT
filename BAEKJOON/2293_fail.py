import sys
sys.setrecursionlimit(10**6)
read=sys.stdin.readline

n,k=map(int,read().split())
coins=[]
for _ in range(n):
	coins.append(int(read()))
visit=[0]*n
check_list=[]
cnt=0


def dfs(val):
	global cnt,visit
	
	if val==k:
		if visit not in check_list:
			check_list.append(visit[:])
			cnt+=1
		return

	
	for i,c in enumerate(coins):
		if val+c<=k:
			visit[i]+=1
			dfs(val+c)
			visit[i]-=1

dfs(0)
print(cnt)