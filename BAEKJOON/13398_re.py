import sys
read=sys.stdin.readline

n=int(read())
arr=list(map(int,read().split()))					

dp1=[0]*n
dp2=[0]*n

dp1[0]=arr[0]
for i in range(1,n):
	dp1[i]=max(dp1[i-1]+arr[i],arr[i])

dp2[0]=arr[0]
for i in range(1,n):
	dp2[i]=max(dp1[i-1],dp2[i-1]+arr[i])
print(dp1,dp2)
ret=-(sys.maxsize-1)

for i in range(n):
	ret=max(ret,dp1[i],dp2[i])
print(ret)