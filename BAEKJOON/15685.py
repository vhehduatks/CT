import sys

read=sys.stdin.readline

N=int(read())
dragon_map=[[[] for _ in range(101)] for _ in range(101)]

direction={
	'right':0,
	'up':1,
	'left':2,
	'down':3
}

def init_func(i,j,d):
	if d==direction['right']:
		return [i,j+1]
	elif d==direction['up']:
		return [i-1,j]
	elif d==direction['left']:
		return [i,j-1]
	elif d==direction['down']:
		return [i+1,j]
	else:
		print('never reach here')

def rotate_clock90(y,x,b,a):
	b=-b
	y=-y
	x_=(y-b)+a
	y_=-(x-a)+b
	return -y_,x_

def make_dragon(j,i,d,g):
	temp_dragon=[[i,j]]
	temp_dragon.append(init_func(i,j,d))
	temp=[]
	while g:
		end_i,end_j=temp_dragon[-1]	
		for td_i,td_j in reversed(temp_dragon):
			next_i,next_j=rotate_clock90(td_i,td_j,end_i,end_j)
			if next_i!=end_i or next_j!=end_j:
				temp.append([next_i,next_j])
		temp_dragon+=temp
		g-=1
	return temp_dragon
	

for _ in range(N):
	j,i,d,g=map(int,read().split())
	dragon=make_dragon(j,i,d,g)
	for i,j in dragon:
		dragon_map[i][j]=1

cnt=0
for i in range(100):
	for j in range(100):
		if dragon_map[i][j] and dragon_map[i+1][j] and dragon_map[i][j+1] and dragon_map[i+1][j+1]:
			cnt+=1

print(cnt)