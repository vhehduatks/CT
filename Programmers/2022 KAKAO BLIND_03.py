
# def record_func(records):
# 	for line in records:
# 		dtiem,carnum,info=line[0],line[1],line[2]

gra={}

def intime_func(carnum,intime,outtime):
	intime=list(map(int,intime.split(':')))
	outtime=list(map(int,outtime.split(':')))
	ret=(outtime[0]-intime[0])*60
	ret+=outtime[1]-intime[1]
	return ret

def money_func(fees,time_sum):
	
	if time_sum<fees[0]:
		ret=fees[1]
		return ret
	else:
		ret=fees[1]
		remain=time_sum-fees[0]
		ret=ret+(remain//fees[2] if remain%fees[2]==0 else remain//fees[2]+1)*fees[3]
	return ret


total_time={}
in_out={}
def solution(fees, records):
	ret={}
	for line in records:
		dtime,carnum,info=line.split()
		if info=='IN':
			gra[carnum]=dtime
			in_out.setdefault(carnum,0)
			total_time.setdefault(carnum,0)
			in_out[carnum]+=1
		elif info=='OUT':
			temp_time_sum=intime_func(carnum,gra[carnum],dtime)
			total_time[carnum]+=temp_time_sum
			in_out[carnum]-=1

	for carnum,time_sum in total_time.items():
		total=money_func(fees,time_sum)
		ret.setdefault(carnum,total)
		# ret[carnum]+=total
		
	for line in reversed(records):
		dtime,carnum,_=line.split()
		if in_out[carnum]:
			in_out[carnum]-=1
			time_sum=intime_func(carnum,dtime,'23:59')
			time_sum+=total_time[carnum]
			total=money_func(fees,time_sum)
			ret[carnum]=total
	
	ret_=[]
	for carnum,money in ret.items():
		ret_.append([carnum,money])
	
	result=[]
	for r in sorted(ret_):
		result.append(r[1])

	return result

fees_=[180,5000,10,600]
record_=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees_,record_))