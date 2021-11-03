import sys
read=sys.stdin.readline

T=int(read())

# def recur(n,k,before):
#     ret=0
#     if k>n:
#         return 0
#     if k==n:
#         return 1
#     for next in range(1,4):
#         if next!=before:
#             ret+=recur(n,k+before,next)

#     return ret

# for _ in range(T):
#     n=int(read())
#     cnt=recur(n,0,0)
#     print(cnt)

for _ in range(T):
    n=int(read())
    q=list()
    cnt=0
    q.append((0,0))
    while q:
        k,before=q.pop(0)
        if(k+before)==n:
            cnt+=1
            continue
        if(k+before)>n:
            continue

        for next in range(1,4):
            if next!=before:
                q.append((k+before,next))
    print(cnt)