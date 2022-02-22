
# def record_func(records):
# 	for line in records:
# 		dtiem,carnum,info=line[0],line[1],line[2]

car_list=[0]*10000
gra={}

def intime_func(carnum,dtime):
	intime=gra[carnum]
	intime=list(map(int,intime.split(':')))
	dtime=list(map(int,dtime.split(':')))
	ret=(dtime[0]-intime[0])*60
	ret+=dtime[1]-intime[1]
	return ret

def money_func(fees,time_sum):
	
	if time_sum<fees[0]:
		ret=fees[1]
		return ret
	else:
		ret=fees[1]
		remain=time_sum-fees[0]
		ret=ret+(remain//fees[2]+1)*fees[3]
	return ret



def solution(fees, records):
	ret=[]
	out_cars=[]
	for line in records:
		dtime,carnum,info=line.split()
		if info=='IN':
			gra[carnum]=dtime
		elif info=='OUT':
			time_sum=intime_func(carnum,dtime)
			total=money_func(fees,time_sum)
			ret.append([carnum,total])
			out_cars.append(carnum)
	
	for line in records:
		dtime,carnum,_=line.split()
		if not carnum in out_cars:
			time_sum=intime_func(carnum,'24:00')
			total=money_func(fees,time_sum)
			ret.append([carnum,total])
	
	ret=sorted(ret,key=lambda x:x[0])

	return ret

fees_=[180,500,10,600]
record_=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees_,record_))