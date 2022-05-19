import sys
read=sys.stdin.readline

# 5455++
n=read().strip()
not_working=int(read())
if not_working:
	error_num=list(map(int,read().split()))

sub=abs(int(n)-100)

result_plus=''
ptr=0
while ptr<len(n):
	temp=int(n[ptr])
	while temp in error_num and temp<10:
		temp+=1
	if temp<10:
		result_plus+=str(temp)
	ptr+=1

result_minus=''
ptr=0
while ptr<len(n):
	temp=int(n[ptr])
	while temp in error_num and 0<=temp:
		temp-=1
	if 0<=temp:
		result_minus+=str(temp)
	ptr+=1

if result_plus:
	p_val=abs(int(n)-int(result_plus))
else:
	p_val=sys.maxsize-1
if result_minus:
	m_val=abs(int(n)-int(result_minus))
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
			print(len(result_plus)+p_val)
		else:
			print(len(result_minus)+m_val)

