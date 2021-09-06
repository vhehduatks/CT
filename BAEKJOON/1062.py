import sys
from string import ascii_lowercase
read=sys.stdin.readline

N,K=map(int,read().split())
Word=[]
for _ in range(N):
    Word.append(read().strip()[4:-4])

base=['a','n','t','i','c']
ascii=list(ascii_lowercase)
new_ascii=[a for a in ascii if a not in base]

def comb(n,arr):
    ret=[]
    result=base[:]

    def recur(nextarr):
        if len(result)==n:
            ret.append(result[:])
            return
        if not nextarr:
            return
        
        temp=nextarr[:]
        for k in nextarr:
            result.append(k)
            temp.remove(k)
            recur(temp)
            result.pop()
    recur(arr)
    return ret

if K>5:

    comb_list=comb(K,new_ascii)

    ret_list=[]
    for c in comb_list:
        ret=0
        for w in Word:
            state=True
            temp=list(w)
            for t in temp:
                if t not in c:
                    state=False
                    break
            if state:
                ret+=1
        ret_list.append(ret)

    print(max(ret_list))
elif K>25:
    print(N)
else:
    print(0)
