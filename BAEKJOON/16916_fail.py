import sys
read=sys.stdin.readline

full_str=read().strip()
P=read().strip()
part_str=[]
state=False

for i in range(len(full_str)):
    for j in range(i+1,len(full_str)+1):
        if P==full_str[i:j]:
            state=True
            break

print(1 if state else 0)
