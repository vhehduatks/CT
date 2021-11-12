import sys
read=sys.stdin.readline
N,K=map(int,read().split())
objw=[]
objv=[]
for _ in range(N):
    w,v=map(int,read().split())
    objw.append(w)
    objv.append(v)
dp=[[-1]*(N+1) for _ in range(K+1)]

def top_down(weight,i):
    if i==N:
        return 0
    if dp[weight][i]!=-1:
        return dp[weight][i]
    
    dp[weight][i]=max(top_down(weight,i+1),top_down(weight+objw[i],i+1)+objv[i]) if weight+objw[i]<=K else top_down(weight,i+1)

    return dp[weight][i]

print(top_down(0,0))