# dfs 로 탐색하면서 다음 원소에 2나 3을 곱해서 가능하면 ret에 추가
import sys
read=sys.stdin.readline

N=int(read())
arr=list(map(int,read().split()))

ret=[]
visit=[False]*(N+1)
def dfs(n):
	if len(ret)==N:
		print(' '.join(list(map(str,ret))))
		exit()
		return
	
	for i in range(N):
		if not visit[i]:
			temp=arr[i]
			if n*2==temp or n//3==temp and n%3==0:
				ret.append(temp)
				visit[i]=True
				dfs(temp)
				ret.pop()
				visit[i]=False

for i in arr:
	ret.append(i)
	dfs(i)
	ret.pop()