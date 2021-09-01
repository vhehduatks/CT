import sys
read=sys.stdin.readline

H,W=map(int,read().split())
block=list(map(int,read().split()))
rain=0

for i in range(len(block)):
    left_high=max(block[:i+1])
    right_high=max(block[i:])
    rain+=(min(left_high,right_high)-block[i])

print(rain)