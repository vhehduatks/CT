import sys
sys.setrecursionlimit(10**6)
from itertools import permutations
read=sys.stdin.readline

N=int(read())
temp=list(map(int,read().split()))
scvs=[temp[i] if i<N else 0 for i in range(3)]
heats=[9,3,1]

dp=[[[0]*61 for _ in range(61)] for _ in range(61)]

def top_down(scv1,scv2,scv3):
	scv1=scv1 if scv1>=0 else 0
	scv2=scv2 if scv2>=0 else 0
	scv3=scv3 if scv3>=0 else 0
	if not scv1+scv2+scv3:	
		return 0

	if dp[scv1][scv2][scv3]:
		return dp[scv1][scv2][scv3]

	ret=sys.maxsize
	for h in permutations(heats,3):
		ret=min(ret,top_down(scv1-h[0],scv2-h[1],scv3-h[2])+1)
	dp[scv1][scv2][scv3]=ret
	return ret


top_down(scvs[0],scvs[1],scvs[2])

print(dp[scvs[0]][scvs[1]][scvs[2]])


