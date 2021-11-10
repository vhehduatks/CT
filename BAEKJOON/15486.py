import sys
read=sys.stdin.readline

N=int(read())
Time=[]
Pay=[]
for _ in range(N):
    t,p=map(int,read().split())
    Time.append(t)
    Pay.append(p)
DP=[0]*(N+1)

for i in reversed(range(N)):
    if i+Time[i]<N+1:
        DP[i]=max(DP[i+1],DP[i+Time[i]]+Pay[i])
    else:
        DP[i]=DP[i+1]

print(DP[0])