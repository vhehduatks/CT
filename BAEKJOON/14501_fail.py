"""
time[i]
price[i]

dp[i]=max(dp[i],price[i]+dp[j]) # 단 dp[j]부터 추가하려는 price[j]의 차이는 time[j] 만큼 생겨야 함

"""

import sys
read=sys.stdin.readline
N=int(read())
time=[]
price=[]

for _ in range(N):
    time_,price_=map(int,read().split())
    time.append(time_)
    price.append(price_)
if N>1:
    dp=[0]*15
    dp[0]=price[0]
    for i in range(1,N):
        for j in range(i):
            if i-j>=time[j]:
                dp[i]=max(dp[i],price[i]+dp[j])

    ret=-(sys.maxsize-1)
    for i in range(N):
        if i+time[i]<=N:
            ret=max(ret,dp[i])

    print(ret)
else:
    print(price[0] if time[0]==1 else 0)


