'''
알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.
'''

from socket import AddressFamily
import sys
from collections import deque

read=sys.stdin.readline

N,M=map(int,read().split())
graph=[list(map(int,list(read().strip()))) for _ in range(N)]
visit=[[False]*M for _ in range(N)]
cost=[[0]*N for _ in range(N)]
cost[N-1][M-1]=sys.maxsize
Q=deque()
Q.append((0,0,0))
d_i=[0,0,1,-1]
d_j=[1,-1,0,0]

while(Q):
    i,j,c=Q.popleft()
    
    for k in range(4):
        n_i=i+d_i[k]
        n_j=j+d_j[k]
        if n_i==N-1 and n_j==M-1:
            cost[n_i][n_j]=min(c,cost[n_i][n_j])
        if 0<=n_i<N and 0<=n_j<M and not visit[n_i][n_j] and graph[n_i][n_j]==0 :
            n_c=c
    

            Q.append((n_i,n_j,n_c))
            visit[n_i][n_j]=True

def is_corner(i,j):
    for k in range(4):
        n_i=i+d_i[k]
        n_j=j+d_j[k]
        if n_i==N-1 and n_j==M-1:
            cost[n_i][n_j]=min(c,cost[n_i][n_j])
        if 0<=n_i<N and 0<=n_j<M:
            pass


print(cost[N-1][M-1])


