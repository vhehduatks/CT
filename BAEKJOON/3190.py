import sys
read=sys.stdin.readline

N=int(read())
K=int(read())
graph=[[False]*(N+1) for _ in range(N+1)]

for _ in range(K):
	i,j=map(int,read().split())
	graph[i][j]=True

L=int(read())
snake=[(1,1)]
pres_d=1
cnt=0
direction={'up':0,'right':1,'down':2,'left':3}

def is_apple(i,j):
	global graph
	if graph[i][j]:
		graph[i][j]=False
		return True
	return False

def is_collapse(i,j):
	if i<=0 or N<i or j<=0 or N<j:
		return True
	if (i,j) in snake:
		return True
	return False

def move(snake,pres_d,sec):
	global cnt
	while sec>cnt:
		cnt+=1
		if pres_d==direction['up']:
			pres_head_i,pres_head_j=snake[-1]
			
			next_head_i,next_head_j=pres_head_i-1,pres_head_j
			if is_collapse(next_head_i,next_head_j):
				return cnt
			if is_apple(next_head_i,next_head_j):
				
				snake.append((next_head_i,next_head_j))
				continue
			snake.append((next_head_i,next_head_j))
			snake.pop(0)
			
		elif pres_d==direction['right']:
			pres_head_i,pres_head_j=snake[-1]
			
			next_head_i,next_head_j=pres_head_i,pres_head_j+1
			if is_collapse(next_head_i,next_head_j):
				return cnt
			if is_apple(next_head_i,next_head_j):
				
				snake.append((next_head_i,next_head_j))
				continue
			snake.append((next_head_i,next_head_j))
			snake.pop(0)
			
		elif pres_d==direction['down']:
			pres_head_i,pres_head_j=snake[-1]
			
			next_head_i,next_head_j=pres_head_i+1,pres_head_j
			if is_collapse(next_head_i,next_head_j):
				return cnt
			if is_apple(next_head_i,next_head_j):
				
				snake.append((next_head_i,next_head_j))
				continue
			snake.append((next_head_i,next_head_j))
			snake.pop(0)
			
		elif pres_d==direction['left']:
			pres_head_i,pres_head_j=snake[-1]
			
			next_head_i,next_head_j=pres_head_i,pres_head_j-1
			if is_collapse(next_head_i,next_head_j):
				return cnt
			if is_apple(next_head_i,next_head_j):
				
				snake.append((next_head_i,next_head_j))
				continue
			snake.append((next_head_i,next_head_j))
			snake.pop(0)
			
		else:
			print('never reach here')
	return 0
		
order=[]

for _ in range(L):
	s,d=read().split()
	s=int(s)
	order.append((s,d))


m=0
while 1:
	if order:
		s,d=order.pop(0)
	else:
		s=sys.maxsize-1
	m=move(snake,pres_d,s)
	if m:
		break
	if d=='L':
		pres_d-=1
		pres_d%=4
	elif d=='D':
		pres_d+=1
		pres_d%=4

print(m if m else cnt)
