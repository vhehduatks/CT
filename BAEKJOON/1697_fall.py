"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

"""

import sys
sys.setrecursionlimit(10**5)

read = sys.stdin.readline

N,K=map(int,read().split())

visit=[False]*100001
cnt=0
fast_time=sys.maxsize-1
def dfs(n):
	global cnt,fast_time
	if n==K:
		fast_time=min(fast_time,cnt)
		return
	if fast_time<cnt:
		return
	if n<0 or n>100000:
		return
	
	
	if visit[n]==False:
		cnt+=1
		visit[n]=True
		dfs(n+1)
		dfs(n-1)
		dfs(n*2)
		visit[n]=False
		cnt-=1


	pass

dfs(N)
print(fast_time)