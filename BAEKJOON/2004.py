maxn=200
dp=[0]*(maxn+1)
dp[0]=1
dp[1]=1
for n in range(2,maxn+1):
	dp[n]=dp[n-1]*n
print("over")
i,j=map(int,input().split())

temp=str(dp[i]/(dp[j]*dp[i-j]))
cnt=0
for c in reversed(temp):
	if c!='0':
		break
	cnt+=1	

print(cnt)