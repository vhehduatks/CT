import sys
from unittest import result
read=sys.stdin.readline


N,L,R,X=map(int,read().split())

arr=list(map(int,read().split()))
cnt=0
ret=[]
visit=[False]*N

def dfs(depth):
	global cnt
	if len(ret)>=2:
		if L<=sum(ret) and sum(ret)<=R:
			temp=sorted(ret)
			if abs(temp[0]-temp[-1])>=X:
				cnt+=1
				if len(ret)==N:
					return
	for i in range(depth,len(arr)):
		if not visit[i]:
			ret.append(arr[i])	
			visit[i]=True
			dfs(i+1)
			visit[i]=False
			ret.pop()
dfs(0)
print(cnt)

	
