import sys
read=sys.stdin.readline	

N=int(read())
cost=[]

for _ in range(N):
	cost.append(list(map(int,read().split())))

MAX_VAL=sys.maxsize-1


color=[0,1,2]
def recur(prev,pres,depth):
	if depth==N-1:
		tempcost=MAX_VAL
		for c in color:
			if c!=prev and c!=First_color:
				tempcost=min(tempcost,cost[depth][c])
		return tempcost

	# if dp[depth]!=-1:
	# 	return dp[depth]
	
	retcost=MAX_VAL
	
	for next_color in color:
		if next_color != pres:
			retcost=min(retcost,recur(pres,next_color,depth+1))+cost[depth][pres]
	
	dp[depth]=retcost
	return retcost

res=MAX_VAL

for First_color in color:
	dp=[-1]*N
	res=min(res,recur(1,1,0))	
print(res)