import sys
read=sys.stdin.readline

N,K=map(int,read().split())
waiting=list(map(int,read().split()))
multtap=[]
cnt=0

for i,w in enumerate(waiting):
    if w in multtap:
        continue
    if len(multtap)<N:
        multtap.append(w)
        continue

    cnt+=1
    idxs=[]
    for m in multtap:
        try:
            idx=waiting[i:].index(m)
        except:
            idx=999
            idxs.append(idx)
            break    
        idxs.append(idx)
    
    del multtap[idxs.index(max(idxs))]
    multtap.append(w)

print(cnt)
