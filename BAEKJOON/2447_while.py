N=int(input())

graph=[[' ']*N for _ in range(N)]

graph[0][:3]=graph[2][:3]=['*']*3
graph[1]=['*',' ','*']

num=3
while num<=N:
	for i in range(0,num,num//3):
		for j in range(0,num,num//3):
			if i==num//3 and j==num//3:continue
		
			for k in range(num//3):
				graph[i+k][j:j+num//3]=graph[k][:num//3]
	num*=3

for i in range(N):
	for j in range(N):
		print(graph[i][j],end='')
	print()

