import sys
read=sys.stdin.readline

N=int(read())
arr=list(map(int,read().split()))

dp1=[1]*N
for i in range(N):
    for j in range(i):
        if arr[i]>arr[j]:
            dp1[i]=max(dp1[i],dp1[j]+1)          
dp2=[1]*N
for i in reversed(range(N)):
    for j in range(N-1,i,-1):
        if arr[i]>arr[j]:
                dp2[i]=max(dp2[i],dp2[j]+1)

ret=0
print(dp1,dp2)
for i in range(N):
    ret=max(ret,dp1[i]+dp2[i])
print(ret-1)
"""
17
7 2 1 1 5 2 2 3 2 3 1 2 4 5 1 2 4

정답 6

10
1 5 2 1 4 3 4 5 2 1

정답 7

5
1 2 3 2 1

정답 5

6
1 2 3 5 5 1

정답 5

5
1 2 1 1 1

정답 3

2
999 1000

정답 2

6

1 2 3 3 2 1

정답 5

5

1 3 1 2 1

정답 4

5

1 5 4 2 3

정답 4

7

5 1 6 2 6 2 1

정답 5

9

5 1 6 2 7 3 7 2 1

정답 6

4

1 2 2 1

정답 3

6

1 2 3 2 1 4

정답 5

2

1 1

정답 1

4

1 1 2 1

정답 3

5
5 4 3 2 3

정답 4
"""