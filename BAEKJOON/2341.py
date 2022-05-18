import sys

read=sys.stdin.readline

N,W=map(int,read().split())
arr=[]

for _ in range(N):
	arr.append(int(read()))

dp=[0]*51
convert_list=[]
code_list=[]

def cost_func(convert_val,arr_val,w)->int:
	cost=sys.maxsize-1
	code=0
	min_convert=0
	for i,convert in enumerate([1,86,172,256]):
		temp=abs(arr_val-convert)
		if convert_val==convert:
			if temp+w<cost:
				cost=temp+w
				code=i
				min_convert=convert
		else:
			if temp+3*w<cost:
				cost=temp+3*w
				code=i
				min_convert=convert

	code_list.append(code)
	convert_list.append(min_convert)
	return cost

def binary_search(K, num_list=[1,86,172,256]):  # 일반적인 이진탐색 함수
	left = 0
	right = len(num_list) - 1
	result = 0  # 마지막에 return할 result 값을 선언함
	while left <= right:  # left가 right보다 클 때까지 진행하는 while문을 돌림
		mid = (left + right) // 2  # 중간값은 두개를 더한 것을 2로 나눈 몫
		if K == num_list[mid]:  # 구하고자 하는 K가 리스트의 중간값과 같다면 K를 리턴하고 종료
			return num_list[mid]
		elif K < num_list[mid]:  # elif와 else문은 일반적인 이진 탐색과 크게 다르지 않음
			right = mid - 1
		else:
			left = mid + 1

	if K not in num_list:  # left가 right보다 커졌을 때 while문이 종료됨. num_list에 K가 없을 경우에
		low = abs(K - num_list[right])  # 현재 right의 인덱스가 더 작으므로, 작은 인덱스쪽의 절대값을 K - num_list[right]으로 줬고 이를 low로 선언함
		high = abs(num_list[left] - K)  # 현재 left의 인덱스가 더 크므로, 큰 인덱스쪽의 절대값을 num_list[left] - K로 줬고 이를 high로 선언함

		if low <= high:  # 더 작은 인덱스의 절대값이 더 큰 인덱스의 절대값보다 "같거나" 작을 때:
			result = num_list[right]    # 결과값 result에 num_list[right]을 부여함
		else:  # 더 작은 인덱스의 절대값이 더 큰 인덱스의 절대값보다 클 때:
			result = num_list[left]  # 결과값 result에 num_list[left]을 부여함

		return result # 최종 결과값 result를 반환합니다.


convert_list.append(binary_search(arr[0]))

dp[0]=abs(convert_list[0]-arr[0])+2*W

for i in range(1,N):
	dp[i]=dp[i-1]+cost_func(convert_list[i-1],arr[i],W)

print(dp[N-1])
print(code_list)