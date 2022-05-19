import sys
read=sys.stdin.readline

n=int(read())
m=int(read())

if m:
	error_nums=list(map(int,read().split()))
	cnt=close_val=sys.maxsize-1
	# 희망채널이 500,000 이고 에러번호가 1,2,3,4,5,6,7,8 일경우 900,000 에서 400,000 번 - 누른 경우가 최적해이다. 그럼 범위는 900,001로 해도 될듯?->가능
	for i in range(600001):
		error_in=False
		for s in str(i):
			if int(s) in error_nums:
				error_in=True
				break
		if not error_in:
			if cnt>abs(n-i):
				cnt=abs(n-i)
				close_val=i

	cnt=min(len(str(close_val))+cnt,abs(n-100))
	print(cnt)

else:
	min_val=min(len(str(n)),abs(n-100))
	print(min_val)