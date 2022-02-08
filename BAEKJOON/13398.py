import sys
read=sys.stdin.readline
MIN_VAL=(-1)*(sys.maxsize-1)
N=int(read())
arr=list(map(int,read().split()))

def part_sum(arr,state):
	if not arr:
		return 0
	retsum=[MIN_VAL]*len(arr)
	retsum[0]=arr[state]	
	ans=arr[state]
	for i in range(1,len(arr)):
		print(arr[i])
		retsum[i]=max(arr[state*i],retsum[i-1]+arr[state*i])	
		ans=max(ans,retsum[i])
	return ans


all_sum=sum(arr)

for del_ptr in range(len(arr)):
	left_arr=arr[:del_ptr]
	right_arr=arr[del_ptr:]

	left_sum=part_sum(left_arr,0)
	right_sum=part_sum(right_arr,-1)
	all_sum=max(all_sum,left_sum+right_sum)

print(all_sum)