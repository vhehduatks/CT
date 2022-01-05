import sys
sys.setrecursionlimit(10**6)
read=sys.stdin.readline
MAX_VAL=sys.maxsize-1

N=int(read())
cost=[]
for _ in range(N):
	cost.append(list(map(int,read().split())))

color=[0,1,2]
def top_down(depth,pres):
	if depth==N-1:
		if pres==first:
			return MAX_VAL
		else:
			return cost[depth][pres]
	
	if dp[depth][pres]:
		return dp[depth][pres]
	ret=MAX_VAL
	for next in color:
		if next!=pres:
			ret=min(ret,top_down(depth+1,next)+cost[depth][pres])
	
	dp[depth][pres]=ret
	return ret
res=MAX_VAL
for first in color:
    dp=[[0]*3 for _ in range(N)]
    res=min(res,top_down(0,first))	
print(res)