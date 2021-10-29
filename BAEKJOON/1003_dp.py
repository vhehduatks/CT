import sys
read=sys.stdin.readline

T=int(read())
dp_0=[-1]*41
dp_1=[-1]*41

def top_down(N):
    if N==0:
        return 1
    if N==1:
        return 0
    if dp_0[N]>0:
        return dp_0[N]
    
    dp_0[N]=top_down(N-2)+top_down(N-1)

    return dp_0[N]

def bottom_up(N):
    dp_1[0]=0
    dp_1[1]=1
    for i in range(2,N+1):
        dp_1[i]=dp_1[i-2]+dp_1[i-1]
    return dp_1[N]

for _ in range(T):
    n=int(read())
    print(top_down(n),bottom_up(n))