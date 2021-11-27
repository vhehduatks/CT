import sys
sys.setrecursionlimit(10**6)
read=sys.stdin.readline

N=int(read())

di=[-2,-1,1,2,2,1,-1,-2]
dj=[1,2,2,1,-1,-2,-2,-1]
def top_down(pi,pj):
	if pi==edi and pj==edj:
		return 0
	if dp[pi][pj]!=-1:
		return dp[pi][pj]
	
	dp[pi][pj]=sys.maxsize-1
	for i in range(8):
		nexti=pi+di[i]
		nextj=pj+dj[i]
		if 0<=nexti and nexti<nm and 0<=nextj and nextj<nm:
			dp[pi][pj]=min(dp[pi][pj],top_down(nexti,nextj)+1)

	return dp[pi][pj]

for _ in range(N):
	nm=int(read())
	dp=[[-1]*300 for _ in range(300)]
	sti,stj=map(int,read().split())	
	edi,edj=map(int,read().split())
	cnt=top_down(sti,stj)
	print(cnt)
	dp=[]
