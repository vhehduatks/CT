import sys
read=sys.stdin.readline

T=int(read())
for _ in range(T):
    n=int(read())
    arr=[list(map(int,read().split())) for _ in range(2)]
    dp=[[-1]*n for _ in range(2)]
    dp[0][0]=arr[0][0]
    dp[1][0]=arr[1][0]
    dp[0][1]=dp[1][0]+arr[0][1]
    dp[1][1]=dp[0][0]+arr[1][1]
    for i in range(2,n):
        dp[0][i]=max(dp[1][i-1],dp[1][i-2])+arr[0][i]
        dp[1][i]=max(dp[0][i-1],dp[0][i-2])+arr[1][i]
    print(max(dp[0][n-1],dp[1][n-1]))
    