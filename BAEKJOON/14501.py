import sys
read=sys.stdin.readline

N=int(read())

sechedule_list=[list(map(int,read().split())) for _ in range(N)]
dp=[0]*(N+1)
def recur(day):
	if day>=N:
		return 0
	profit=0
	if dp[day]:
		profit=dp[day]
	if day+sechedule_list[day][0]<=N:
		profit=max(profit,recur(day+sechedule_list[day][0])+sechedule_list[day][1])
	profit=max(profit,recur(day+1))

	dp[day]=profit

	return profit

recur(0)

print(max(dp))