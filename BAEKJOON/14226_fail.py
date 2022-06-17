"""
영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

영선이는 이미 화면에 이모티콘 1개를 입력했다. 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.

화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
화면에 있는 이모티콘 중 하나를 삭제한다.

모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다. 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.
"""

import sys
from collections import deque
read=sys.stdin.readline

s=int(read())
Q=deque()
visit=[False]*1001

def bfs(n):
	Q.append((n,0,0))
	visit[n]=True
	while Q:
		global cnt
		Q_,cnt_,clip_=Q.popleft()
		if Q_==s:
			return cnt_
		
		if clip_ and Q_+clip_<=1000 and visit[Q_+clip_]==False:
			Q.append((Q_+clip_,cnt_+1,clip_))
			visit[Q_+clip_]=True

		if 0<Q_ and Q_<=1000:
			Q.append((Q_,cnt_+1,Q_))


		if Q_-1>=0	and visit[Q_-1]==False:
			Q.append((Q_-1,cnt_+1,clip_))
			visit[Q_-1]=True


print(bfs(1))
