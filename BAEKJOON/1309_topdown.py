import sys
sys.setrecursionlimit(10**6)
N=int(input())
dp=[[0]*2 for _ in range(100001)]

def top_down(num,depth):
    if depth==N:
        return 1 

    if dp[depth][num]:
        return dp[depth][num]
    ret=0
    if not num:
        ret+=top_down(0,depth+1)+top_down(1,depth+1)+top_down(1,depth+1)
    elif num==1:
        ret+=top_down(0,depth+1)+top_down(1,depth+1)
    dp[depth][num]=ret%9901
    return ret

print(top_down(0,0)%9901)