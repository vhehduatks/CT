n,m=map(int,input().split())

def cnt_func(num,val):
	i=val	
	cnt=0
	while i<=num:
		cnt+=num//i	
		i*=val
	return cnt
# n_pair=min(cnt_func(n,5),cnt_func(n,2))
# nm_pair=min(cnt_func(n-m,5),cnt_func(n-m,2))+min(cnt_func(m,5),cnt_func(m,2))
print(min(cnt_func(n,5)-(cnt_func(n-m,5)+cnt_func(m,5)),cnt_func(n,2)-(cnt_func(n-m,2)+cnt_func(m,2))))