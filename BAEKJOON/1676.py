maxn=501
dp=[0]*(501)
dp[0]=1
dp[1]=1
for n in range(2,501):
	dp[n]=dp[n-1]*n	

N=list(str(dp[int(input())]))

cnt=0
for c in reversed(N):
	if c!='0':
		break	
	cnt+=1
print(cnt)