import sys

read=sys.stdin.readline

n=int(read())
m=int(read())
if m:
	error_num=list(map(int,read().split()))

	result_plus=result_minus=n

	sub=abs(100-n)

	error_status=True
	while error_status:
		result_plus%=10
		temp=str(result_plus)
		in_error=False
		for t in temp:
			if int(t) in error_num:
				result_plus+=1
				in_error=True
				break
		if in_error:
			continue
		error_status=False	

	error_status=True
	while error_status:
		result_minus%=10
		temp=str(result_minus)
		in_error=False
		for t in temp:
			if int(t) in error_num:
				result_minus-=1
				in_error=True
				continue
		if in_error:
			continue
		error_status=False

	if result_plus:
		p_val=abs(n-result_plus)
	else:
		p_val=sys.maxsize-1
	if result_minus:
		m_val=abs(n-result_minus)
	else:
		m_val=sys.maxsize-1

	result_list=[p_val,m_val,sub]

	min_idx=result_list.index(min(result_list))
	if min_idx==2:
		print(sub)
	else:
		if result_list[min_idx]==0:
			print(n)
		else:
			if min_idx==0:
				print(len(str(result_plus))+p_val)
			else:
				print(len(str(result_minus))+m_val)
else:
	print(len(str(n)))