import sys
read=sys.stdin.readline
T=int(read())
wheels=[list(map(int,list(read().strip()))) for _ in range(T)]
K=int(read())


def rotate_func(num,d):

	right_tooth=wheels[num][2]
	left_tooth=wheels[num][-2]
	temp_rotate=wheels[num][d*-1:]+wheels[num][:d*-1]

	if not visit[num]:
		visit[num]=True
		#첫번쨰일경우
		if num==0:
			if right_tooth!=wheels[num+1][-2]:
				rotate_func(num+1,d*-1)
		#마지막일경우
		elif num==T-1:
			if left_tooth!=wheels[num-1][2]:
				rotate_func(num-1,d*-1)

		else:
			if left_tooth!=wheels[num-1][2]:
				rotate_func(num-1,d*-1) 
			if right_tooth!=wheels[num+1][-2]:
				rotate_func(num+1,d*-1)
			
		wheels[num]=temp_rotate
	
		

# 12시는 0번 인덱스, 2번과 -2번 인덱스가 접점
for _ in range(K):
	wheel_num,rotate=map(int,read().split())
	visit=[False]*T
	rotate_func(wheel_num-1,rotate)

ret=0
for w in wheels:
	ret+=w[0]

print(ret)