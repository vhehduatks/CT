import sys
sys.setrecursionlimit(100000)
read=sys.stdin.readline


def top_down(prev,i):
    if i==n-1:
        if prev==-1:
            return max(arr[0][i],arr[1][i])
        elif prev==0:
            return arr[1][i]
        else:
            return arr[0][i]
    if dp[i]!=-1:
        return dp[i]    

    dp[i]=0

    if prev==-1:
        dp[i]=max(
            dp[i],
            top_down(1,i+1)+arr[1][i],
            top_down(0,i+1)+arr[0][i]
            )
    elif prev==0:
        dp[i]=max(
            dp[i],
            top_down(1,i+1)+arr[1][i],
            top_down(-1,i+1)
            )
    else:
        dp[i]=max(
            dp[i],
            top_down(0,i+1)+arr[0][i],
            top_down(-1,i+1)
            )
    return dp[i]


T=int(read())
for _ in range(T):
    n=int(read())
    arr=[]
    for _ in range(2):
        arr.append(list(map(int,read().split())))
    dp=[-1]*n
    print(top_down(-1,0))
