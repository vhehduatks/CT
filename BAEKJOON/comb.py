
def comb(n,Arr):
    ret=[]
    result=[]
    def recur(nextarr):
        if len(result)==n:
            ret.append(result[:])
            return
        if not nextarr:
            return

        
        temp=nextarr[:]
        for i in nextarr:
            
            result.append(i)
            temp.remove(i)
            recur(temp)
            result.pop()
    
    recur(Arr)
    return ret

print(comb(2,[1,2,3,4]))