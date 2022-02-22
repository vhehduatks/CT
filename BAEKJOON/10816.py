import sys
read=sys.stdin.readline
N=int(read())
input_list=list(map(int,read().split())) # -100만 +100만 사이의 숫자들
M=int(read())
num_list=[0]*20000002 # 
for i in input_list:
	num_list[i]+=1
my_list=list(map(int,read().split()))
for i in my_list:
	print(num_list[i],end=' ')


