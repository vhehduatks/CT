import sys
read=sys.stdin.readline
MAX_VAL=sys.maxsize-1

N=int(read())
cost=[]
for _ in range(N):
	cost.append(list(map(int,read().split())))
color=[0,1,2]
dp=[[0]*N for _ in range(3)]
def recur(first,prev,pres,depth):
	if depth==N-1:
		if pres==first:
			return MAX_VAL
		tempcost=MAX_VAL
		for c in color:
			if c!=first and c!=prev:
				tempcost=min(tempcost,cost[depth][c])

		return tempcost

	if dp[first][depth]:
		return dp[first][depth]

	ret=MAX_VAL

	for nextc in color:
		if nextc != pres:
			ret=min(ret,recur(first,pres,nextc,depth+1)+cost[depth][pres])
	
	dp[first][depth]=ret
	return ret

res=MAX_VAL

res=recur(1,1,1,0)
print(res)