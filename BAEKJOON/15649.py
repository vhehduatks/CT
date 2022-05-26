import sys

N,M=map(int,sys.stdin.readline().split())

ret=[]
visit=[False]*(N+1)
def recur():
	if len(ret)==M:
		print(' '.join(list(map(str,ret))))
		return
	for i in range(1,N+1):
		if visit[i]==False:
			ret.append(i)
			visit[i]=True
			recur()
			ret.pop()
			visit[i]=False

recur()
