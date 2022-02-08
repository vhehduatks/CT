import sys
read=sys.stdin.readline

N,M,x,y,K=map(int,read().split())
graph=[]

for _ in range(N):
	graph.append(list(map(int,read().split())))

order=list(map(int,read().split()))

dice={
	'on':0,
	'under':0,
	'up':0,
	'down':0,
	'right':0,
	'left':0,
	'i':x,
	'j':y
}
direction={
	'N':3,
	'S':4,
	'W':2,
	'E':1
}
def dice_swap(d):
	temp=0
	if d==direction['E']:
		next_i,next_j=dice['i'],dice['j']+1
		if is_out(next_i,next_j):
			return -1
		else:
			dice['i'],dice['j']=next_i,next_j
		temp=dice['right']
		dice['right']=dice['on']
		dice['on']=dice['left']
		dice['left']=dice['under']
		dice['under']=temp
	elif d==direction['W']:
		next_i,next_j=dice['i'],dice['j']-1
		if is_out(next_i,next_j):
			return -1
		else:
			dice['i'],dice['j']=next_i,next_j
		temp=dice['left']
		dice['left']=dice['on']
		dice['on']=dice['right']
		dice['right']=dice['under']
		dice['under']=temp
	elif d==direction['N']:
		next_i,next_j=dice['i']-1,dice['j']
		if is_out(next_i,next_j):
			return -1
		else:
			dice['i'],dice['j']=next_i,next_j
		temp=dice['up']
		dice['up']=dice['on']
		dice['on']=dice['down']
		dice['down']=dice['under']
		dice['under']=temp
	elif d==direction['S']:
		next_i,next_j=dice['i']+1,dice['j']
		if is_out(next_i,next_j):
			return -1
		else:
			dice['i'],dice['j']=next_i,next_j
		temp=dice['down']
		dice['down']=dice['on']
		dice['on']=dice['up']
		dice['up']=dice['under']
		dice['under']=temp
	else:
		print('never reach here')
	return dice['on']

def is_under_side_zero(i,j):
	global graph
	if graph[i][j]==0:
		graph[i][j]=dice['under']
	else:
		dice['under']=graph[i][j]
		graph[i][j]=0
def is_out(i,j):
	if i<0 or N<=i or j<0 or M<=j:
		return True
	return False

result=[]
def rolling(go_to):
	dice_on=dice_swap(go_to)
	if dice_on>=0:
		is_under_side_zero(dice['i'],dice['j'])
		result.append(str(dice_on))
	

while 1:
	if order:
		go_to=order.pop(0)
	else:
		break
	rolling(go_to)

print('\n'.join(result))

