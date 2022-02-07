import sys
read=sys.stdin.readline

N=int(read())
arr=list(map(int,read().split()))

dp=[1]*N
for i in range(N):
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))
