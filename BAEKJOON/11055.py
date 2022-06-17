import sys
read=sys.stdin.readline

# 증가하는 수열은 한번만 증가해야 하기 때문에 중복제거를 위해 최대값만 비교한다.
N=int(read())
arr=list(map(int,read().split()))

# 1,100 -> 
dp=arr[:]

for i in range(N):
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+arr[i])

print(max(dp))
