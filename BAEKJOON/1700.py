import sys
read=sys.stdin.readline

multtap=[]

N,K=map(int,read().split())
waiting=list(map(int,read().split()))


count=0
for i,w in enumerate(waiting):
    if w in multtap:
        pass
    elif len(multtap)<N:
        multtap.append(w)
    else:
        alluse=True
        for m in multtap:
            if not m in waiting[i:]:
                count+=1
                multtap.remove(m)
                multtap.append(w)
                alluse=False
                break
        if alluse:
            count+=1
            for w2 in reversed(waiting):
                if w2 in multtap:
                    multtap.remove(w2)
            multtap.append(w)
print(count)

