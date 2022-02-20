import sys
import copy
read=sys.stdin.readline

N,M=map(int,read().split())
office_map=[]
cctv=[]

for i in range(N):
    temp=list(map(int,read().split()))
    office_map.append(temp)
    for j,t in enumerate(temp):
        if t==6 or t==0:
            pass
        else:
            cctv.append([i,j,t])

i_=[-1,1,0,0] #상, 하, 좌, 우  
j_=[0,0,-1,1]

cctv_dict={
    1:[[0],[1],[2],[3]],
    2:[[0,1],[2,3]],
    3:[[0,2],[0,3],[1,2],[1,3]],
    4:[[0,2,3],[1,2,3],[0,1,3],[0,1,2]],
    5:[[0,1,2,3]]
}

def is_out(i,j):
    if i<0 or N<=i or j<0 or M<=j:
        return True
    return False

def cctv_func(cd,temp_map,temp_cctv):
    for case in cd:
        next_i,next_j=temp_cctv[0],temp_cctv[1]
        while 1:
            next_i,next_j=next_i+i_[case],next_j+j_[case]
            if not is_out(next_i,next_j):
                if temp_map[next_i][next_j]==6:
                    break
                else:
                    temp_map[next_i][next_j]=temp_cctv[2]
            else:
                break


def dfs(depth,map):
    global min_val
    if depth==len(cctv):
        cnt=0
        for i in range(N):
            cnt+=map[i].count(0)
        min_val=min(min_val,cnt)
        return
    
    temp_map=copy.deepcopy(map)
    temp_cctv=cctv[depth]
    for cdict in cctv_dict[temp_cctv[2]]:
        cctv_func(cdict,temp_map,temp_cctv)
        dfs(depth+1,temp_map)
        temp_map=copy.deepcopy(map)


min_val=sys.maxsize-1
dfs(0,office_map)
print(min_val)