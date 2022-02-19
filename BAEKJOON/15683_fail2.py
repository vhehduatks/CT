import sys
read=sys.stdin.readline

N,M=map(int,read().split())

cctv=[]
wall=[]
real_map=[]
for i in range(N):
    temp=list(map(read().split()))
    real_map.append(temp)
    for j,t in enumerate(temp):
        if t!=0:
            if t==6:
                wall.append([i,j])
            else:
                cctv.append([i,j,t])
direction={'up':0,'right':1,'down':2,'left':3}

def is_stuck(i,j):
    if real_map[i][j]==6:
        return True
    elif i<0 or N<=i or j<0 or M<=j:
        return True
    return False

def cctv_func(i,j,temp_map,d,cn):
    while 1:
        if d==direction['up']:
            next_i,next_j=i-1,j
            if not is_stuck(next_i,next_j):
                temp_map[next_i][next_j]=cn
            else:
                break
        elif d==direction['right']:    
            next_i,next_j=i,j+1
            if not is_stuck(next_i,next_j):
                temp_map[next_i][next_j]=cn
            else:
                break
        elif d==direction['down']:
            next_i,next_j=i+1,j
            if not is_stuck(next_i,next_j):
                temp_map[next_i][next_j]=cn
            else:
                break
        elif d==direction['left']:
            next_i,next_j=i,j-1
            if not is_stuck(next_i,next_j):
                temp_map[next_i][next_j]=cn
            else:
                break

cctv_num={1:4,2:2,3:4,4:4,5:1}
def recur():
    pass

for c in cctv:
    pass
    
